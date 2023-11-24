# Comfyui-GLM3Prompt

参考来源：https://www.bilibili.com/read/cv27685652/



### 使用说明

使用[ChatGLM3-6B](https://github.com/THUDM/ChatGLM3)进行对话，支持连续对话



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

![image](https://github.com/Lin1031/Comfyui-GLM3Prompt/assets/44975556/790a0194-a950-4db0-92e5-cf637a0a3834)


注意：默认从 [Hugging Face Hub](https://huggingface.co/THUDM/chatglm3-6b)拉取模型

#### 5. 修改模型调用方式（可选）
![image](https://github.com/Lin1031/Comfyui-GLM3Prompt/assets/44975556/c82a305b-1b03-43ee-8c33-b91b94aaede4)


1. 标准：模型以 FP16 精度加载，运行上述代码需要大概 13GB 显存

   ```
   self.model = AutoModel.from_pretrained(self.model_path, trust_remote_code=True, device='cuda')
   ```

2. 如果你的 GPU 显存有限，可以尝试以量化方式加载模型（代码默认使用）

   ```
   self.model = AutoModel.from_pretrained(self.model_path, trust_remote_code=True).quantize(4).cuda()
   ```

3. 其他参考官方文档（mac、多卡、cpu）

   https://github.com/THUDM/ChatGLM3/tree/main#%E4%BD%8E%E6%88%90%E6%9C%AC%E9%83%A8%E7%BD%B2


![image-20231117214413053](https://s2.loli.net/2023/11/17/g42ucDVnXSANOCT.png)


#### 效率基于3080ti
首次加载模型需要20s左右，不同长度的提示词模型效率不同，越长的提示词需要的时间不同。量化模型大约使用4g显存。默认开启即调用模型后释放显存，若提示词有修改重新调用模型。关闭后则模型一直缓存在显存中，有上下文功能，且多次调整提示词速度更快
![image](https://github.com/Lin1031/Comfyui-GLM3Prompt/assets/44975556/3f4879dc-6cbe-419c-81b0-cc3aad67449f)


![image](https://github.com/Lin1031/Comfyui-GLM3Prompt/assets/44975556/ec9c840b-19ca-4295-989c-45f3499c48b9)

![image](https://github.com/Lin1031/Comfyui-GLM3Prompt/assets/44975556/3ff5a4eb-2251-47b2-88cd-9b96881f124f)

