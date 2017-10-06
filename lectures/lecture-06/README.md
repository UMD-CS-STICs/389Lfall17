# Lecture 6: Message Queues

In class, we went through a short demo of SQS queues. Here are the commands that I ran through:

### Setup

First, create three separate terminal sessions. SSH onto a Vagrant box, so that you can use your AWS credentials. Let's give these sessions names: let one be the "sender" and the other two be "receiver 1" and "receiver 2".

#### Creating a Queue

Next, you will need to create a SQS queue. You could do this via the CLI or the Management Console, but I'd recommend the latter for learning purposes.

To do this, open the SQS service then select "Create New Queue". Give it a name and select "Standard Queue". Click "Configure Queue" and change the Visibility Timeout to 15s. You can leave all of the other settings on their defaults, though feel free to play around with them.

### Sending a Message

With the sender session, go ahead and first grab the URL of the queue you just created.

```
vagrant ~$ aws sqs list-queues
```

Now, send a new message into this queue:

```
vagrant ~$ aws sqs send-message --queue-url "<queue url>" --message-body "Hello World"
```

You can send as many messages as you'd like.

### Receiving a Message

With receiver 1, let's pull out this message.

```
vagrant ~$ aws sqs receive-message --queue-url "<queue url>" --wait-time-seconds 20
```

This will long-poll for a new message from the queue, though it should return immediately.

Run this command again and notice how it takes ~15s from when you first ran it till when the message shows up again.

### Multiple Messages in the Queue

Go ahead and publish another message (with a different message!) with the sender and then request a message once on each of the two receivers. You'll see that they both get unique results. Best effort ordering in standard queues means that whichever sender ran the receive command first will most likely receive the first message you published.

### Mark Messages as Processed

Usually, a message will only be pulled out once and then marked as processed by the receiver. To do this, we need to delete the message from the queue.

When you receive a message from SQS, it will return a "Receipt Handle" which uniquely identifies the request you made. You supply this in your delete request to specify which message to remove from the queue.

```
vagrant ~$ aws sqs delete-message --queue-url "<queue url>" --receipt-handle "<receipt handle>"
```

Now, attempt to query for the message and notice how the message is no longer returned, no matter how long you poll for.

### At-Least-Once Delivery

We can create a situation where a message is "processed" multiple times.

Let's assume the queue contains a single message.

With sender 1, receive the message and "process" it.

With sender 2, long poll until that message is made visible again and begin "processing" it.

Now, both senders have processed the message and can both independently mark it as deleted.

Essentially, this case will occur if a message takes longer than the Visibility Timeout to process a request.

### Wrapping Up

If you have any questions, feel free to ask on Piazza.
