<p align="center">
    <h3 align="center">Simple Barber</h3>
</p>

<p align="center">Simple reservation system for barbers written in Next.js that uses FastAPI with SQLAlchemy as the API backend.</p>

<br/>

## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and FastAPI as the API backend.

## How It Works

The Python/FastAPI server is mapped into to Next.js app under `/api/`.

This is implemented using `next.config.js` rewrites to map any request to `/api/:path*` to the FastAPI API, which is hosted in the `/api` folder.

On localhost, the rewrite will be made to the `127.0.0.1:8000` port, which is where the FastAPI server is running.

## Getting started

Create a new user and a database in your PostgreSQL and modify variables inside `api/database.py`:
```
DB_USER = "simple-barber-user"
DB_PASS = "simple-barber-pass"
DB_NAME = "simple-barber-db"
```

Note: In case you are not using PostgreSQL, edit `DATABASE_URL` variable accordingly.

Migrate data:
```
TODO
```

Generate your own secret for password hashing:
```
openssl rand -hex 32
```
and update `SECRET_KEY` variable inside `api/passlib.py`.

Install dependencies:
```
npm install
```

Run development server:
```
npm run dev
```

Default credentials for addministration are:
- username: admin
- password: admin

## Developing Locally

You can clone & create this repo with the following command

```bash
npx create-next-app simple-barber --example "https://github.com/malyjak/simple-barber"
```

## Deployment

You can clone & deploy it to the Vercel with one click:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fmalyjak%2Fsimple-barber%2Ftree%2Fdevelop)

## Credits

Mapping the FastAPI server to Next.js was inspired by this [Vercel demo](https://github.com/digitros/nextjs-fastapi").