FROM python:3.10.4-slim

RUN mkdir /dna-nucleotide-count-app

WORKDIR /dna-nucleotide-count-app

COPY . /dna-nucleotide-count-app

RUN pip install -r requirements

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]

CMD [ "dnanucleotidecountapp.py" ]

