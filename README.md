# FastAPI Text Summarizer

## Setup

1. Create a virtual environment:
    ```
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
2. Install dependencies:
    ```
    pip install requirements.txt
    ```
3. Create .env file:
    ```
   OPENAI_API_KEY=your_api_key
   ```
4. Run the application:
    ```
    uvicorn main:app --reload
    ```
5. Test the endpoint:
    * Send a POST request to ```http://127.0.0.1:8000/summarize``` with a JSON body containing the text to be
      summarized.

## Example of usage:
* Post request to ```http://127.0.0.1:8000/summarize```
   ```
    {
  "text": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
    }
    ```
* Endpoint response:
   ```
   {
  "summary": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building. Its base is square, measuring 125 metres (410 ft) on each side. It is the second tallest free-standing structure in France after the Millau Viaduct."
   }
   ```