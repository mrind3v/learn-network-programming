Typing `google.com` into your browser triggers a multi-step process called **DNS resolution**, which translates the human-readable domain name into an IP address that a computer can understand. This process relies on a distributed, hierarchical system of servers. Here is a step-by-step breakdown:

---

### The Journey of a DNS Query

#### 1. The Local Resolver

When you hit Enter, your browser first checks its own **cache** for the IP address of `google.com`. If it's not there, it asks the operating system (OS). The OS also checks its cache. If the IP is still not found, your computer sends a request to a **recursive resolver**. This resolver is typically managed by your Internet Service Provider (ISP) or a public service like Google's 8.8.8.8. Its job is to find the IP address for you, handling all the subsequent steps. It's the "librarian" that goes and finds the right book for you.

#### 2. The Root Server

If the recursive resolver doesn't have `google.com` in its cache, it starts the search at the top of the DNS hierarchy. It sends a query to one of the **13 root name servers**. The root server doesn't know the IP address for `google.com`, but it knows where to find information for all **Top-Level Domains (TLDs)**, like `.com`, `.org`, and `.net`. It responds to the resolver with the IP address of the TLD server responsible for the `.com` domain.

#### 3. The TLD Server

With the IP address of the `.com` TLD server in hand, the recursive resolver sends another query, this time asking for the IP address of `google.com`. The TLD server, which manages all `.com` domains, doesn't have the final IP address. However, it knows which server is the **authoritative name server** for `google.com`. It responds to the resolver with the IP address of that specific server.

#### 4. The Authoritative Name Server

Finally, the recursive resolver sends a query to the **authoritative name server** for `google.com`. This server is the definitive source for all DNS records for that domain. It holds the actual mapping between the domain name (`google.com`) and its IP address (e.g., `142.250.187.206`). It returns this IP address to the recursive resolver.

---

### Getting the Results Back

#### 5. The Response and Caching

The recursive resolver now has the IP address. It caches this information for a specified period (its **Time-to-Live or TTL**) and then returns the IP address to your computer. Your computer also caches the IP address. This caching is crucial, as it makes future requests for `google.com` much faster since the entire resolution process doesn't have to be repeated.

#### 6. The Final Connection

Your browser, with the IP address of the Google server, can now initiate a standard network connection. It sends a request (e.g., an HTTP GET request) to `142.250.187.206`. The Google server receives the request and sends the webpage data back to your browser, which then renders the page for you.

