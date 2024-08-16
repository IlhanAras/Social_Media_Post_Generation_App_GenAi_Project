from fastapi import FastAPI
from pydantic import BaseModel
import io
import base64

from ImageGenerator import ImageGenerator
from llm import llmclass 


txt_generator = llmclass()

# python -m uvicorn fastapi_app:app --reload
app = FastAPI()

class QueryRequest(BaseModel):
    query: dict
    model_option_name:str
    
 
@app.post("/query/image")
async def get_image(request: QueryRequest):
    img_generator = ImageGenerator(model_id=request.model_option_name)
    image = img_generator.generate_social_media_image(request.query)
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return {"response": img_str}   



@app.post("/query/text")
async def get_text(request: QueryRequest):
    
    text_result = txt_generator.generate_content(request.query)
    return {"response": text_result}
    