import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/christophleitner/api/zenserp'

mcp = FastMCP('zenserp')

@mcp.tool()
def search(q: Annotated[str, Field(description='Query String (keyword)')],
           device: Annotated[Union[str, None], Field(description="Which device to use: ['desktop', 'mobile']")] = None,
           tbm: Annotated[Union[str, None], Field(description="Set to 'isch' for image results")] = None,
           location: Annotated[Union[str, None], Field(description='location for the search engine')] = None,
           search_engine: Annotated[Union[str, None], Field(description='The url of the search engine to query')] = None,
           num: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get a SERP'''
    url = 'https://zenserp.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'zenserp.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'device': device,
        'tbm': tbm,
        'location': location,
        'search_engine': search_engine,
        'num': num,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
