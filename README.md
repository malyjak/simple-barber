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

Install dependencies:
```
npm install
```

Run development server:
```
npm run dev
```

## Authentication

[Clerk](https://clerk.com/) is used for authentication to access the administration area of the application. Once you are signed into your account, create a new application named "simple-barber". Select just "Email" and unselect all the other options when creating the application.

Then create `.env.local` file in the root directory and store your Clerk's secrets there.

## Developing Locally

You can clone & create this repo with the following command

```bash
npx create-next-app simple-barber --example "https://github.com/malyjak/simple-barber"
```

## Deployment

You can clone & deploy it to Vercel with one click:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fmalyjak%2Fsimple-barber%2Ftree%2Fdevelop)

## Credits

Mapping the FastAPI server to Next.js was inspired by this [Vercel demo](https://github.com/digitros/nextjs-fastapi").