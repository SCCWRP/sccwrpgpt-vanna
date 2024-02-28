# SCCWRP Vanna AI Data Search Tool

Uses the Vanna AI to search data in our internal database

Essentially we feed it schema information and it creates queries for us to execute and retrieve data

Still in the beginning experimental stages

In order for this to work, it needs a folder called models, and that folder for this particular application contains something to do with ChromaDB

The user which the application runs with needs read/write/(maybe also execute??) access to ~/.cache (whichever the home directory is) (In our case its /var/www/.cache)

We are using OpenAI via Vanna, with ChromaDB and Postgres
Documentation:
[https://vanna.ai/docs/postgres-openai-standard-chromadb.html](https://vanna.ai/docs/postgres-openai-standard-chromadb.html)

Our implementation is not very similar to what is found in that documentation, since this is a flask app, and their documentation is using a jupyter notebook

This current repository is based off this one, which is an implementation in a flask app, and this repository may as well be a fork of that repository:
[https://github.com/vanna-ai/vanna-flask](https://github.com/vanna-ai/vanna-flask)





