'''
Description:  
Author: Huang J
Date: 2025-05-26 15:19:54
'''

import os
import asyncio
from pathlib import Path
from webseer import Seer
from transformers import AutoModel, AutoModelForCausalLM, AutoTokenizer

# 单关注点
async def single_focus():
    focus = '实体经济'
    urls = ['http://www.news.cn/','https://www.news.cn/fortune/20250508/131ecdbba88943a586e3526fba1b9e80/c.html'] 
    await webseer.crawler(focus=focus,urls=urls,llm=None,tokenizer=None)

# 多关注点
async def multi_focus():
    focus_urls = {
                    '实体经济信息':['https://www.news.cn/fortune/20250508/131ecdbba88943a586e3526fba1b9e80/c.html','http://www.news.cn/'],
                    '农业机械化':['https://www.news.cn/20250504/b43aae5ed4144369886a3fd57b250c39/c.html','https://www.news.cn/20250430/b46d19c2a3fb43a19dc2edc7cbdc1b4e/c.html','https://www.news.cn/20250422/dbbd2ac346a84aa9899b437b149ccbbc/c.html','https://www.news.cn/20250409/2266159883cb41e6877a538719f7a2cc/c.html','https://www.news.cn/20250330/d204b33b7dac4b32bf9d5bf562c891d4/c.html','https://www.news.cn/20250320/2ce97ba1331c4ae28608a3b1c4bcca41/c.html']
                }
    await webseer.multicrawler(focus_urls=focus_urls,llm=None,tokenizer=None)

if __name__ == "__main__":

    # 数据库信息
    host = ''
    port = 3306
    user = ''
    password = ''

    encode_model = AutoModel.from_pretrained("jinaai/jina-embeddings-v3", trust_remote_code=True).to('mps')
    
    # readertokenizer = AutoTokenizer.from_pretrained("jinaai/ReaderLM-v2")
    # readerlm = AutoModelForCausalLM.from_pretrained("jinaai/ReaderLM-v2").to('cuda')

    # tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
    # llm = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct").to('cuda')

    logger_dir = ''
    if not logger_dir:
        current_dir = os.path.dirname(Path(__file__))
        logger_dir = os.path.join(current_dir, 'logs')
        if not os.path.exists(logger_dir):
            os.makedirs(logger_dir, exist_ok=True)
    
    webseer = Seer(host,port,user,password,logger_dir,encode_model,extract_method='selector',max_request_retries=3)
    
    asyncio.run(single_focus())
    # asyncio.run(multi_focus())