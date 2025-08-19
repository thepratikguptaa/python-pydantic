from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]
    
class BlogPost(BaseModel):
    title: str = Field(
        ..., # required
        min_length=10,
        max_length=50,
        description="The title of the blog post",
        )
    content: str
    image_url: Optional[str] = None