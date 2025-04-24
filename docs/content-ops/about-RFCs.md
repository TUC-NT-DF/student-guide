# About RFCs

Definitions first: a *software contract* is an API, or a protocol, or some other formalized interaction that allows two otherwise unconnected components of a system to work together [1].

All libraries and products implement contracts, explicit or implicit. Contracts may be documented (using formal prose like **RFCs**, ideally), or embedded in code (less than ideal) [1].

*A contract may have multiple independent and competing implementations* [1].

## Contracts

!!! hint
    The following content is cited from Pieter Hintjens Book *ZeroMQ*, Chapter 7. For a more complete and comprehensive explanation see [2]. The book is very much recommended.

A good software architecture depends on contracts, and the more explicit they are, the better things scale.

So what is a contract in a distributed system? There are, in my experience, two types of contract:

- The APIs to client applications. The APIs need to be as absolutely simple, consistent, and familiar as possible.
- The protocols that connect the pieces.

Writing contracts is perhaps the most difficult part of large-scale architecture. A good contract (be it an API, a protocol, or a rental agreement) has to be simple, unambiguous, technically sound, and easy to enforce.

Like any technical skill, it’s something you have to learn and practice.

## Contracts are hard

I’ll try to summarize what I’ve learned from my experience as a protocol writer:

- Start simple, and develop your specifications step-by-step. Don’t solve problems you don’t have in front of you.
- Make nothing for which you cannot demonstrate an immediate need. Your specification solves problems; it does not provide features. Make the simplest plausible solution for each problem that you identify.
- Implement your protocol *as you build it*, so that you are aware of the technical consequences of each choice.
- Test your specification on other people *as you build it*. Your best feedback on a specification is when someone else tries to implement it without the assumptions and knowledge that you have in your head.
- Be prepared to throw it out and start again as often as needed. Plan for this, by layering your architecture so that, e.g., you can keep an API but change the underlying protocols.

## How to write contracts (RFCs)

When you start to write a specification document, stick to a consistent structure so that your readers know what to expect. Here is the structure I use:

- Cover section: with a one-line summary, URL to the spec, formal name, version, who to blame.
- The change process: i.e., how can I as a reader fix problems in the specification?
- Use of language: MUST, MAY, SHOULD, etc., with a reference to RFC 2119.
- Maturity indicator: is this an experimental, draft, stable, legacy, or retired version?
- Goals of the protocol: what problems is it trying to solve?
- References: to other documents, protocols, etc.

The RFCs of our research group can be found in this [repository](https://gitlab.hrz.tu-chemnitz.de/DioneCG/RFC).

If you want to write an RFC, please start by using our [templates](https://gitlab.hrz.tu-chemnitz.de/DioneCG/RFC/tree/master/templates).

## RFC lifecycle

The lifecycle of an RFC should follow the [COSS - Consensus Oriented Specification System](https://rfc.unprotocols.org/spec:2/COSS/).

## References

[1] The End of Software Versions, <http://hintjens.com/blog:85>

[2] ZeroMQ, Pieter Hintjens, O'Reilly Media, Inc., 2013, Print ISBN-13: 978-1-4493-3406-2
