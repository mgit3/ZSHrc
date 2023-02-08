# Use an official Redis image as base
FROM redis:latest

# Copy the custom redis.conf file to the image
COPY redis.conf /usr/local/etc/redis/redis.conf

# Set the environment variable for the password
ENV REDIS_PASSWORD=mysecretpassword

# Expose the Redis port
EXPOSE 6379

# Start Redis using the custom redis.conf file
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]

