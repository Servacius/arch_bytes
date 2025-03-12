from pydantic import BaseModel, Field

class TopicRequest(BaseModel):
    topic: str = Field(..., title="The topic for which to generate a bite-sized data", description="The topic for which to generate a data on Software Architecture", example="Microservices")