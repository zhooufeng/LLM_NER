{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Downloading (…)l-00001-of-00007.bin:   2%|▏         | 31.5M/1.83G [1:51:48<106:25:04, 4.69kB/s]\n",
      "Loading checkpoint shards: 100%|██████████| 7/7 [00:14<00:00,  2.04s/it]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "你好👋！我是人工智能助手 ChatGLM2-6B，很高兴见到你，欢迎问我任何问题。\n"
     ]
    }
   ],
   "source": [
    "from transformers import AutoTokenizer, AutoModel\n",
    "tokenizer = AutoTokenizer.from_pretrained(\"../chatglm2-6b\", trust_remote_code=True)\n",
    "models = AutoModel.from_pretrained(\"../chatglm2-6b\", trust_remote_code=True, device='cuda')\n",
    "models = models.eval()\n",
    "response, history = models.chat(tokenizer, \"你好，我想听你讲个故事\", history=[])\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ChatGLM2",
   "language": "python",
   "name": "chatglm2-6b"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.17"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
