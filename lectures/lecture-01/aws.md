# Introduction to AWS

### What is Cloud Computing?

- Let's consider the time before cloud computing. Say you want to start the next AirBnB. You want to host a website to attract interest, so how do you do that? You would have to set up a server farm in your garage. You'll need to estimate your traffic, understand the characteristics of your code (memory, CPU, etc.) and order servers, routers, cabling, storage, etc. and usually wait a few weeks and shell out a large inital capital investment. Then you have to set it up and test it, load your software, configure the servers, patch security vulnerabilities, etc.
- What happens if you underestimate? You'll have a "success disaster".
- What happens if you overestimate? You're paying for capacity that you don't need.
- Cloud computing abstracts away this process of setting up infrastructure -- servers, power, cooling, storage, routers, etc. This is known as Infrastructure as a Service (IaaS).
- Many providers also make available other services beyond IaaS, like software-as-a-service (SaaS) such as Polly (text -> speech) or platform-as-as-service (PaaS) such as Elastic Beanstalk (like Heroku). 
- If they are confusing, think build IaaS, buy SaaS, and deploy onto PaaS.
- Providers benefit from economies of scale of these services, and those benefits are usually passed on to the consumer.
- Providers also usually make it possible to deploy globally.
- Significantly reduces the initial capital required to get started on an idea. This has been key for startup innovation, since it enables entrepreneurs to conduct experiments where they only pay for the capacity that they use, rather than having to predict usage without any data. If the experiment fails, the entrepreneur can move on.
	- Uber, Airbnb are all examples of startups that started on AWS and were able to scale incredibly fast thanks to cloud computing.
	- Segment, pivoted a dozen times before settling on their current idea.
- The main public cloud computing providers are AWS, Microsoft Azure and Google Cloud. Each have different specialties.
- When working in a cloud environment, you are working with commodity hardware at scale. Therefore, the most important thing to keep in mind is the well-known saying from Werner Vogel, who is the CTO of Amazon, that "Everything fails all the time".

### What is AWS?

- AWS is the dominant public cloud computing provider, about 90% of the compute capacity.
- As of this morning, provides [100 different products](https://aws.amazon.com/products/) -- everything from compute to developer tools and a cloud-based customer service center.
- Back in 2003, internal Amazon engineers proposed that they generalize their architecture and sell their excess capacity as a service.
- The first service, SQS, was made available in 2004.
- Grew rapidly, by 2010 all of Amazon.com had moved over.

### Why should I learn AWS?

- The fastest growing public cloud computing platform on the planet.
- A large majority of tech companies are on a public cloud, with the notable exceptions of extremely large companies (Facebook, f.e.) which run their own hardware.
- A background in AWS, or other cloud providers, for that matter, is not usually taught at the university level. Instead it is learned on the job, or through side projects. Therefore, by taking this class and working on the projects, you'll develop a skillset that will set you apart from the competition and open up new opportunities.
