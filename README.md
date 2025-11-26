# Day 6 - Fraud Alert Voice Agent

This repository contains the implementation of the Fraud Alert Voice Agent for Day 6 of the 10 Days of Voice Agents challenge.

## Overview

This project implements a fraud alert voice agent for a fictional bank that contacts customers about suspicious transactions on their accounts. The agent verifies the customer's identity, describes the suspicious transaction, and asks if the customer made the transaction. Based on the customer's response, the agent marks the case as safe or fraudulent and updates the database accordingly.

## Features

- Loads fraud cases from a JSON database
- Verifies customer identity using security questions
- Describes suspicious transactions in detail
- Handles customer confirmation/denial of transactions
- Updates fraud case status in the database
- Uses LiveKit Agents framework with Deepgram STT, Google LLM, and Murf TTS

## Prerequisites

- Python 3.8+
- Node.js 16+
- LiveKit account and credentials
- Deepgram API key
- Google Cloud credentials
- Murf API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/adixists/ten-days-of-voice-agents-day6.git
   cd ten-days-of-voice-agents-day6
   ```

2. Install Python dependencies:
   ```bash
   pip install livekit-agents livekit-plugins-deepgram livekit-plugins-google livekit-plugins-murf
   ```

3. Install Node.js dependencies (for frontend):
   ```bash
   npm install
   ```

## Configuration

1. Copy `.env.example` to `.env.local` and fill in your credentials:
   ```bash
   cp .env.example .env.local
   ```

2. Edit `.env.local` with your actual credentials:
   ```
   LIVEKIT_URL=wss://your-livekit-url
   LIVEKIT_API_KEY=your-api-key
   LIVEKIT_API_SECRET=your-api-secret
   DEEPGRAM_API_KEY=your-deepgram-api-key
   GOOGLE_APPLICATION_CREDENTIALS=path-to-your-google-credentials.json
   MURF_API_KEY=your-murf-api-key
   ```

## Running the Agent

1. Start the backend agent:
   ```bash
   python run_agent.py
   ```
   or alternatively:
   ```bash
   cd src && python -m agent dev
   ```

2. In a separate terminal, start the frontend:
   ```bash
   npm run dev
   ```

3. Open your browser to `http://localhost:3000` (or the port shown in the terminal)

## Testing Different Scenarios

The agent handles three main scenarios:

1. **Confirmed Safe**: Customer verifies their identity and confirms they made the transaction
2. **Confirmed Fraud**: Customer verifies their identity but denies making the transaction
3. **Verification Failed**: Customer fails to correctly answer the security question

The fraud cases are stored in `fraud_cases.json` and are updated with the outcome after each call.

## Database Structure

The fraud cases are stored in a JSON file with the following structure:

```json
{
  "userName": "John",
  "securityIdentifier": "12345",
  "cardEnding": "4242",
  "case": "pending_review",
  "transactionName": "ABC Industry",
  "transactionTime": "2025-11-25 14:30:00",
  "transactionCategory": "e-commerce",
  "transactionSource": "alibaba.com",
  "transactionAmount": "$149.99",
  "location": "China",
  "securityQuestion": "What is your mother's maiden name?",
  "securityAnswer": "Smith",
  "outcomeNote": ""
}
```

## Customization

You can modify the fraud cases in `data/fraud_cases.json` to test different scenarios or add new cases.

## License

This project is licensed under the MIT License.