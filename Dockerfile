FROM python:3.10.4-slim

RUN mkdir /dna-nucleotide-count-web-app

WORKDIR /dna-nucleotide-count-web-app

COPY . /dna-nucleotide-count-web-app

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]

CMD [ "dnanucleotidecountapp.py" ]

