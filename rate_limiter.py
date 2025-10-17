"""
Question: 
design a rate-limiting component for Google’s API Gateway.

Each incoming request contains - (user_id, endpoint, timestamp)

Requirements:
- Each user can make no more than K requests in any rolling N-second window.
- Different endpoints may have different limits (e.g., /search = 100 req/10 s, /upload = 10 req/60 s)

Example Rule:
/search: 100 requests per 10 seconds
/upload: 10 requests per 60 seconds

"""

"""
At high level
- Calculate the number of requests per user, per endpoint. If the number of requests is > than K requests in given time then reject the request

Skeleton of the function
- For each end point, we need to increment the number of requests 
- If the total_requests in the given time is greater than K, then reject

"""


"""
Required Data Structures - Definitely require O(1) operations given the scale

- Since it is a rolling window, we can use a deque() to maintain a N-second rolling window and check if the total_requests > K

1. Create a deque. Initialize the values
2. Insert new transaction. 
    - (timestamp, total_requests)
3. Discard new transaction if total_requests > k

"""
from collections import deque, defaultdict

class UserEndpoint:
    def __init__(self):
        self.user_endpoint_dq = defaultdict(deque())
        self.total_requests = 0

class RateLimiter:
    def __init__(self, endpoint, threshold, window):
        self.endpoint = endpoint
        self.threshold = threshold
        self.window = window
        self.user_endpoint = defaultdict(UserEndpoint)


    def on_event(self, user_id, endpoint, timestamp):
        user = self.user_endpoint[user_id]
        dq = user.user_endpoint_dq[endpoint]

        cutoff = timestamp - self.window

        while dq and dq[0][0] < cutoff:
            dq.popleft()
            user.total_requests -= 1


        dq.append((timestamp))
        user.total_requests += 1


        if user.total_requests > self.threshold:
            return "Request Rejected"








        
