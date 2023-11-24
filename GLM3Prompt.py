import gc
import json
from transformers import AutoTokenizer, AutoModel
from comfy.model_management import soft_empty_cache

class GLM3Prompt:
    """
    ChatGLM3接口调用
    """

    def __init__(self):
        self.model_path = "THUDM/chatglm3-6b" # 修改这个路径为本地模型存放路径，不修改会自动下载模型
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(self.model_path, trust_remote_code=True).quantize(4).cuda()
        self.model = self.model.eval()
        self.history = []

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "unload": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("提示词",)

    FUNCTION = "translate"

    # OUTPUT_NODE = False

    CATEGORY = "GLM3Prompt"

    def translate(self, text, unload=False):
        if self.tokenizer:
            reply, self.history = self.model.chat(self.tokenizer, text, history=self.history)
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
            self.model = AutoModel.from_pretrained(self.model_path, trust_remote_code=True).quantize(4).cuda()
            self.model = self.model.eval()
            reply, self.history = self.model.chat(self.tokenizer, text, history=self.history)

        if unload:
            # 清空 tokenizer 和其他字段
            self.tokenizer = None
            self.model = None
            self.history = None
            
            # 垃圾回收和清空缓存
            gc.collect()
            soft_empty_cache()

        
        return (reply,)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "GLM3Prompt": GLM3Prompt
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "GLM3Prompt": "ChatGLM3提示词生成工具"
}
