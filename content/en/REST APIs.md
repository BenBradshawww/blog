+++
title = 'Rest APIs'
date = 2024-10-30
categories = ["Programming Tools"]
tags = ["REST APIs"]
keywords = ["Rest", "REST APIs", "APIs"]
description = "SEO Description Here"
draft = false
[params.math]
  math = true
+++

![Image](images/ante-hamersmit-DSUjNkiRFg0-unsplash.jpg)
[Image by Ante Hamersmit](https://unsplash.com/@ante_kante?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)
## What are APIs

Before we just into the class of Rest APIs it is best to understand what is an API. An API is simply an acronym for application programming interface, a software intermediary that allows two applications to talk to each other.

They are usually explained in terms of a client and a server. The application that sends a request is called the client and the application that sends the response is called the server.

In general when we refer to an API, we often are referring to [web APIs](https://stoplight.io/api-types). These APIs are accessed via a HTTP protocol (see the appendix).

APIs fall into 4 different categories [1]:

- Public APIs: These APIs are available to anyone to use with little to no restriction through registration and authentication. These includes services such as the Spotify API, OpenWather API, and Google Maps API.
- Internal (Private) APIs: These APIs are designed for use by a closed group of API consumers. These often have much greater security than public APIs.
- Partner APIs: These sit between private and public APIs. These often share data between two companies.
- Open APIs: Most Public APIs follow the OpenAI standard which provides guidelines on endpoint naming, data formats, and error messaging.

## API Protocals

Every API has a protocol. This defines how your API will connect to internet and how it will communicate information. There are many different type each with their own set of advantages and drawbacks.

- SOAP APIs: Simple Object Access Protocol (SOAP) is another API protocol which can connect over TCP and SMTP alongside HTTP. As a result, it is more flexible than REST, however it is also more restrictive because it only works with XML data and has more rigid requirements for requests. One advantage of SOAP is its requirement for metadata about the files in the request which results in a standardised protocol able to communicate complex data easily. Consequently, SOAP tends to be a good fit for large and sophisticated applications where reliability takes priority.
- RPC APIs: Remote Procedure Call (RPC) protocols return either XML or JSON responses. RPC calls a method rather than a data source and RPC returns confirmation on whether the function was triggered. RPC API can be thought of as a method to create actions.
- GraphQL APIs: This one isn't really a specific protocol, however, it has a distinct query language. In essence, GraphQL APIs provide clients with higher amounts of flexibility with each query but to achieve this higher flexibility, extensive documentation is needed.
- REST APIs: We'll cover these below.

## REST APIs

The Representational State Transfer (REST) protocol [3] is the most well known protocol. REST simply defines routes with a URL rather than typically having to wrap routes with XML (see the appendix).

APIs that follow the REST architecture style are called REST APIs and the web services that implement REST architectures are called RESTful web services.

## What are the key features of the REST architecture?

- Uniform Interface. Any RESTful web-service must transfer information in a standard format. There are 4 structural constraints on the request. The request must identify resources. Clients should have enough information in the resuource representation to modify or delete the resource if need be. Meta data must be attached to the received information to help the client process the information. The client must also receive information about all other related resources to finish their task.
- Statelessness. Every request is completed independently of all previous request.
- Layered System. The client can connect to intermediaries between the client and server and still be able to receive responses from the server.
- Cacheability. The RESTful web services must support caching where some responses are stored on the clients or intermediary to improve server response time.
- Code on demand. In the REST architecture, servers can transfer software programming code to the client.

## What are the benefits?

There are 3 main benefits of REST APIs.

1. Scalability. RESTful APIs scale efficiently because REST optimises client-server interactions. The REST APIs stateless and well managed caching can reduce load on the server.
2. Flexibility. RESTful web services support client-server separation. Consequently, server and client changes will not require changes to the API.
3. Independence. REST APIs are independent of the technologies they use. Both the client and server application can change without affecting the API design.

## How does it work?

In general, a rest API follows 4 steps.

1. The client sends a request to the server.
2. The server authenticates the request.
3. The server receives and processes the request.
4. The server returns the response to the client.

## What consists of a Restful API Client Request?

Each client request consists of a Uniform Resource Loader (URL) which specifies the path to the resource. This is similar to the website address to enter any browser to visit any webpage and the Restful URL is referred to as the request endpoint.

Since the Restful APIs are implemented with HTTP, the HTTP method will tell the server what to do with the online resource. There are 4 different methods which can be used:

- GET: Clients use GET to access resources at the URL.
- POST: Clients use POST to send data to the server.
- PUT: Clients use PUT to update resources on a server.
- DELETE: Clients use DELETE to delete resources from the server.

Finally, the client request also consists of HTTP headers which consists of the metadata exchanged between the client and server. This can include information about the format of the request and response, information about the request status, and more. Some HTTP headers include data for the POST and PUT HTTP methods. While other headers consist of a list of parameters for what the server needs to do.

## How are Restful APIs verified?

Any web service which uses Restful APIs need to authenticate the requests to verify the identity of the individual who has sent the request. Typically, there are 4 ways to do this.

1. Basic authentication: Here the client sends a username and password in the request header. These details are encoded with base64 for a safe transmission.
2. Bearer authentication: Bearer authentication refers to process of giving access to the token bearer. The token bearers token is usually a string of characters.
3. API keys: Here the server assigns a unique generate value for a first-time client which is used to verification. API keys are less secure because the client has to transmit the key which leaves them vulnerable to network theft.
4. OAuth: OAuth combines passwords and tokens for a highly secure login. The server will identify the first request from the passwords and then will ask for additional tokens for authorisation.

## What does the RESTful request contain?

REST responses consists of:

- A status line to communicate whether the communication was a success or failure. Some common status codes include 200 (generic success response), 201 (POST method success response), 400 (incorrect request the server cannot process), 404 (resource not found).
- A message body which contains the resource. Clients can request information in an XML or JSON format.
- Headers or metadata which provides additional information about the response.

## Appendix

****HTTP:**** A Hypertext Transfer Protocol (HTTP) is used to load webpages using hyperlinks. It is designed to transfer information between network devices.

Internet browsers use HTTP requests as communications platforms to ask for the information needed to load a website. Each HTTP request carries encoded data that carries different types of information, typically this includes

- An HTTP version type.
- A URL.
- An HTTP method.
- An HTTP request header.
- An optional HTTP body.

****XML:**** XML is a software and hardware independent tool for storing or transferring data [2]. In essence, XML is data wrapped around tags.

```xml
<events>
  <event>sale</event>
    <user>Jani</user>
    <item>123456789</item>
    <time>11:59:03</time>
</events>
```

XML looks similar to HTML, however they were designed with different goals. HTML is designed to display data, focusing on how the data looks while XML is designed to carry data.

The key difference between the two is that HTML has predefined tags while XML does not.

## Conclusion

This article introduces the idea of web APIs and briefly covered many of their variants before focussing on the REST API.

## References

  

1. Stoplight. (n.d.). __Types of APIs | Types Of API Calls & REST API Protocol__. [online] Available at: https://stoplight.io/api-types.
2. w3schools (2015). __XML Introduction__. [online] W3schools.com. Available at: https://www.w3schools.com/xml/xml_whatis.asp.
3. Amazon Web Services (2024). __What is RESTful API? - RESTful API Beginner’s Guide - AWS__. [online] Amazon Web Services, Inc. Available at: https://aws.amazon.com/what-is/restful-api/.

‌

‌

‌