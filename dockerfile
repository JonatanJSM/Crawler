FROM python:3.12.1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN python -m nltk.downloader stopwords punkt wordnet omw-1.4
COPY . .
COPY config.example.py /app/solr/config.py
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]