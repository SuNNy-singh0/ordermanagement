from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.product_controller import router as product_router
from controllers.order_controller import router as order_router
from database import Base, engine
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Community Platform API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(product_router)
app.include_router(order_router)

@app.get("/")
async def root():
    return {"message": "Community Platform API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
