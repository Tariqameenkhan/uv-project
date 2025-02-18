# install uv 
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version  # check uv version  
# 
uv init --package first # uv first project 
cd  first
uv add ruff 
uv run ruff check
uv venv .venv # for enviorment
.venv/scripts/activate  
#
uv run main  
uv sync
uv run 1
uv run 2
uv run run_both # both function run 
# ( def run_both
# ()main,hello())
uv run 1; uv run 2 # both function run     
>>
cd ..
clear
#
# litellm install
uv add litellm
pip install python-dotenv # for key protect in .env file
from dotenv import load_dotenv
# Load environment variables from .env
load_dotenv()
os.environ["GEMINI_API_KEY"] =  os.getenv("GEMINI_API_KEY")

# Install Your Project (Editable Mode)
# Before running, install your project in development mode:
pip install -e .
# This allows you to use the scripts defined in pyproject.toml.
#
uv pip install langchain langchain-google-genai # for langchain packages 
uv pip list | findstr langchain-google-genai # check for langchain packages 
>>
python -c "import langchain_google_genai; print(langchain_google_genai.__file__)"
>>
 python -c "import first; print(first.__file__)"
>>
uv pip install -e .