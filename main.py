from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services import summarize_text_Bart

app = FastAPI()


class TextInput(BaseModel):
    text: str


@app.post("/summarize")
async def summarize(input_text: TextInput):
    try:
        # Call summarize_text_Bart function to get the summary
        summary = summarize_text_Bart(input_text.text)
        return {"summary": summary}
    except Exception as e:
        # If an error occurs, raise HTTPException with status code 500 and error details
        raise HTTPException(status_code=500, detail=str(e))
