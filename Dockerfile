# Use the official Node.js image as a base
FROM node:20-alpine

# Set the working directory inside the container
WORKDIR /app


RUN apk add --no-cache git openssh

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .


# Expose the port the app runs on
EXPOSE 3000

# Start the Next.js applicati
CMD ["npm", "run", "dev"]
