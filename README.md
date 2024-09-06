# YouTube Video Summarizer

This is a Flask web application that summarizes YouTube videos using the YouTube Transcript API to extract transcripts and Google Gemini API to generate concise summaries. The application allows users to input a YouTube video URL and receive a summarized version of the video's content.

## Features

- **Automatic Video Transcription**: Extracts transcripts from YouTube videos in multiple languages using the YouTube Transcript API.
- **AI-Powered Summarization**: Utilizes Google Gemini API to generate a concise summary of the video transcript.
- **Multi-language Support**: Attempts to fetch the transcript in multiple languages (English, Hindi, Spanish, French) for broader accessibility.
- **Web Interface**: A simple web interface for users to enter the YouTube video URL and receive the summary.

## Getting Started

### Prerequisites

- **Python 3.7+**: Make sure you have Python installed.
- **Flask**: A web framework for Python.
- **YouTube Transcript API**: A Python library to fetch YouTube video transcripts.
- **Google Gemini API**: API access to generate AI-powered summaries.
- **dotenv**: A package to load environment variables from a `.env` file.
