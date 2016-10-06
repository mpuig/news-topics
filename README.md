# News topic discovery using LDA (Latent Dirichlet Allocation)

-
### Intro

This is an experimental project to play with LDA topic discovery using a scraped version of CNN news. 

### Setup

Create a virtual environment and clone the repository.

```
mkvirtualenv news-topics
git clone https://github.com/mpuig/news-topics
cd news-topics
```

Install the pyLDAvis library using this fork.

```
git clone https://github.com/mpuig/pyLDAvis
cd pyLDAvis
python setup.py install
cd ..
rm -rf pyLDAvis
```

Install the other requirements, needed for the crawling process and also for the analysis one.

```
pip install -r requirements.txt
```

Optionally, at this point, you can launch the crawler.py script and get a recent version of the cnn site. It takes some time to generate a ```cnn.json``` file with the scraped news. If you want to move forward, you can use ```cnn0.json``` or ```cnn1.json```, included with the project.

```
python crawler.py
```

Launch the jupyter notebook and start playing with the topic discovery.

```
jupyter notebook
```
Go to: http://localhost:8888/notebooks/cnn%20topics.ipynb

