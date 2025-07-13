#!/bin/bash

set -e

# Define API URL
API_URL="http://127.0.0.1:5000/api/timeline_post"

# Generate random ID for uniqueness
RANDOM_ID=$(date +%s)

# Timeline post data
NAME="Test User"
EMAIL="test${RANDOM_ID}@example.com"
CONTENT="Testing timeline post number $RANDOM_ID"

# POST request to create timeline post
echo "📤 Sending POST request to create new timeline post..."
POST_RESPONSE=$(curl -s -X POST "$API_URL" \
  -d "name=$NAME" \
  -d "email=$EMAIL" \
  -d "content=$CONTENT")

echo "✅ POST response:"
echo "$POST_RESPONSE"

# Extract ID from response
POST_ID=$(echo "$POST_RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])")

# GET request to retrieve all posts
echo "📥 Sending GET request to retrieve timeline posts..."
GET_RESPONSE=$(curl -s "$API_URL")

echo "✅ GET response:"
echo "$GET_RESPONSE"

# (Bonus) DELETE request to clean up
echo "🗑️ Sending DELETE request for post ID: $POST_ID"
DELETE_RESPONSE=$(curl -s -X DELETE "$API_URL/$POST_ID")

echo "✅ DELETE response:"
echo "$DELETE_RESPONSE"

echo "🎉 All tests completed successfully."
