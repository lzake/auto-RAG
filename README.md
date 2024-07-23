# RAG System

The RAG System is a multi-modal Retrieval-Augmented Generation (RAG) application. It allows users to upload Request for Proposal (RFP) documents and generates responses using OpenAI's GPT models. The system consists of a backend powered by FastAPI and a frontend built with Next.js.

![RAG System UI](/UI.PNG)

## Features

- **Upload RFP Documents**: Users can upload RFP documents in various formats.
- **Generate Responses**: The system processes the uploaded documents and generates responses using OpenAI's GPT-4 model.
- **Modern UI**: Sleek and responsive user interface for seamless interaction.

## Backend

### Setup

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Set up your environment variables** in a `.env` file:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

3. **Run the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```

### Endpoints

- **POST** `/api/upload`: Upload a file and receive a generated text response.
- **GET** `/api/retrieve-docs`: Retrieve documents based on a query.

## Frontend

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

### Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

### Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

### Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out the [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
