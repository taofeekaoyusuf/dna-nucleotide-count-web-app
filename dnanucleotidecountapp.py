# importing useful library
import pandas as pd
import streamlit as st
import altair as alt

from itertools import count
from requests import ReadTimeout


# from PIL import Image

st.write("""
  # WELCOME TO DNA NUCLEOTIDE SEQUENCE COUNT WEB APP

  This web app counts the Nucleotide composition of a DNA Sequence.
""")

# Getting to DNA Sequence data - I have provided a function to read multi-lines of DNA Sequence data for Powerful computers.
# Or simply copy and paste in the text box to count any sample from the dna-sequence.txt file.

# def read_dna_sequence(filename):
#     with open(filename, 'r') as dna_sequence:
#         dna_data = dna_sequence.read().splitlines()
#     return dna_data


# temp_dna_seq = read_dna_sequence("dna-sequence.txt")
temp_dna_seq = "tacacttaacaggcctagggtggtagggccgtcaaatcacatgccgatcttacgacgtcc \
tgagttccgttatcgcgggacgttcacatcctctgacgtacaggggtgactctgaaacct  \
tggtattgttcaatccgagccgttgccggtcgggacgtgtgcaatagaatctcagatgca \
cagcagacaccaaaaccgattgtcgcctccaagcagcgactactgcgttgaatgatgtat \
cagaatcggaaaatgtcggagctagcatctccaactgtacaaactaagggtttgtataag \
cttcaaaagaaaagttcgtagtgacgacgtcctgcctggggcagctctatcaacttttgg \
tcctggagagtgtgtggacgcacatcacaccggccgaagcgagctaacgaaggggcgtag \
gtgaaggaacactcagctcgttatatggaaagcttaagaagattttgtaggtgcgccatg \
gcgcttagtcggccaactcttgcatgtagctagctcacacagatctggaaggcttaccag \
tgttgcttatggacaccgtgtaaagttactctagcatatatagcatcggtagtaacggcg \
cgcataatgtgcctgaatgtctaaatgggggtaaggtcgggcgagcggggcagtgctggg"

st.header('ENTER DNA SEQUENCE: ')
data = st.text_area("Your sequence goes here: >", temp_dna_seq, height=300)

# First approach
st.subheader('Counting Nucleotide using the dictionary count method')


def count_seq(data_seq):
    dict_count = dict([
        ('A', data_seq.count('a')),
        ('T', data_seq.count('t')),
        ('G', data_seq.count('g')),
        ('C', data_seq.count('c')),
    ])
    return dict_count


dna_count = count_seq(data)
dna_count

# 2nd approach
st.subheader('Counting Nucleotide using the string method')


def count_str(seq):
    st.write('There are ' + str(seq['A']) + ' ***Adenine (A)***, ' + str(seq['T']) + ' ***Thymine (T)***, '
             + str(seq['G']) + ' ***Guanine (G)***, and ' + str(seq['C']) + ' ***Cytosine (C)*** in the Nucleotide sample.')


st.write(count_str(dna_count))


# 3rd Approach
st.subheader('Counting Nucleotide using the Pandas DataFrame method')


def df(data):
    data_df = pd.DataFrame.from_dict(data, orient='index')
    data_df = data_df.rename({0: 'Count'}, axis='columns')
    data_df.reset_index(inplace=True)
    data_df = data_df.rename(columns={'index': 'Nucleotides'})

    return data_df


st.write(df(dna_count))

# 4th Approach
st.subheader('Counting Nucleotide using the Bar Chart method')


def plot_bar_chart(data):
    bar_data = df(data)
    dna_bar = alt.Chart(bar_data).mark_bar().encode(
        x='Nucleotides', y='Count'
    ).properties(
        width=alt.Step(100),  # This sets the Bar width property
    )
    return dna_bar


st.write(plot_bar_chart(dna_count))
