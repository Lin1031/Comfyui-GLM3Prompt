# Comfyui-GLM3Prompt

参考来源：https://www.bilibili.com/read/cv27685652/



### 使用说明

使用[ChatGLM3-6B](https://github.com/THUDM/ChatGLM3)进行对话，暂不支持连续对话



#### 1. 安装环境

```
pip install protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate
```

####  2. 下载代码

将 `GLM3Prompt.py` 放入 `/comfyui/custom_nodes` 下

####  3. 下载模型

| Model            | Seq Length | Download                                                     |
| ---------------- | ---------- | ------------------------------------------------------------ |
| ChatGLM3-6B      | 8k         | [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b) |
| ChatGLM3-6B-Base | 8k         | [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b-base) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b-base) |
| ChatGLM3-6B-32K  | 32k        | [HuggingFace](https://huggingface.co/THUDM/chatglm3-6b-32k) \| [ModelScope](https://modelscope.cn/models/ZhipuAI/chatglm3-6b-32k) |

 网盘地址：链接：https://pan.baidu.com/s/1p5j0gQu3Jw_xgdY_UkHtjA?pwd=ljsz 提取码：ljsz 

#### 4. 修改存放模型地址（绝对路径）

将红圈部分改为模型的绝对路径，参考`/root/ComfyUI/models/chatglm3-6b`根据自己实际情况填写

![image-20231117213345560](https://s2.loli.net/2023/11/17/ADIC5rpiLhsznfo.png)

注意：默认从 [Hugging Face Hub](https://huggingface.co/THUDM/chatglm3-6b)拉取模型

#### 5. 修改模型调用方式（可选）

![image-20231117213844645](https://s2.loli.net/2023/11/17/DPFUrubG5KiMfYS.png)

1. 标准：模型以 FP16 精度加载，运行上述代码需要大概 13GB 显存

   ```
   model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True, device='cuda')
   ```

2. 如果你的 GPU 显存有限，可以尝试以量化方式加载模型（代码默认使用）

   ```
   model = AutoModel.from_pretrained("THUDM/chatglm3-6b",trust_remote_code=True).quantize(4).cuda()
   ```

3. 其他参考官方文档（mac、多卡、cpu）

   https://github.com/THUDM/ChatGLM3/tree/main#%E4%BD%8E%E6%88%90%E6%9C%AC%E9%83%A8%E7%BD%B2

   

![image-20231117214413053](https://s2.loli.net/2023/11/17/g42ucDVnXSANOCT.png)

