# PC3 - Pedantic Code Construction Contract

The Pedantic Code Construction Contract (PC3) is an evolution of the GitHub [Fork + Pull Model](https://help.github.com/articles/fork-a-repo/), and the [ZeroMQ C4.1](http://rfc.zeromq.org/spec:22) process, aimed at providing an optimal collaboration model for commercial software projects. PC3 helps an organization build consistently good software, cheaply, and rapidly.

* Name: DioneCG/rfc:001/PC3
* Editor: Matthias Gabriel, Philipp Lindner. Original: [Pieter Hintjens](http://hintjens.com/blog:23)
* Status: stable

## Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119 [1].

The key word "patch" in this document is to be interpreted as "merge request" in GitLab terms.

## Goals

PC3 is meant to provide an optimal collaboration model for commercial software projects. Broadly, PC3 helps an organization build consistently good software, cheaply, and rapidly. It has these specific goals:

* To maximize the scale of the community around a project, by reducing the friction for new Contributors and creating a scaled participation model with strong positive feedbacks;
* To relieve dependencies on key individuals by separating different skill sets so that there is a larger pool of competence in any required domain;
* To allow the project to develop faster and more accurately, by increasing the diversity of the decision making process;
* To support the natural life-cycle of project versions from experimental through to stable, by allowing safe experimentation, rapid failure, and isolation of stable code;
* To reduce the internal complexity of project repositories, thus making it easier for Contributors to participate and reducing the scope for error.
* To reduce the need for meetings, face-to-face presence, and timezone synchronization, by capturing knowledge more accurately.
* To optimize the efficiency of worker resources, by using on-time self-assignment instead of up-front task allocation.


## Preliminaries

* The project SHALL use the git distributed revision control system.
* The project SHALL be hosted on GitLab or equivalent, herein called the "Platform".
* The project SHALL use the Platform issue tracker.
* The project SHOULD have clearly documented guidelines for code style.
* A "Contributor" is a person who wishes to provide a patch, being a set of commits that solve some clearly identified problem.
* A "Maintainer" is a person who merge patches to the project. Maintainers are not developers; their job is to enforce process.
* A "Reviewer" is a person who reviews patches and who has deep familiarity with the code base.
* Contributors SHALL NOT have commit access to the repository unless they are also Maintainers.
* Maintainers SHALL have commit access to the repository.
* Reviewers SHALL NOT have commit access to the repository unless they are also Maintainers.
* Everyone, without distinction or discrimination, SHALL have an equal right to become a Contributor under the terms of this contract.
* The language for written statements SHOULD be English.

## Patch Requirements

* Maintainers, Contributors and Reviewers MUST have a Platform account and SHOULD use their real names or a well-known alias.
* A patch SHOULD be a minimal and accurate answer to exactly one identified and agreed problem.
* A patch MUST adhere to the code style guidelines of the project if these are defined.
* A patch MUST adhere to the "Evolution of Public Contracts" guidelines defined below.
* A patch MUST compile cleanly and pass project self-tests on at least the principle target platform.
* A patch commit message MUST consist of a single short (less than 50 characters) line stating the problem ("Problem: ...") being solved, followed by a blank line and then the proposed solution ("Solution: ...").
* The build process MUST use the CI/CD pipeline.
* A "Correct Patch" is one that satisfies the above requirements.

## Development Process

* Change on the project SHALL be governed by the pattern of accurately identifying problems and applying minimal, accurate solutions to these problems.
* To initiate changes, a user SHALL log an issue on the project Platform issue tracker.
* The user SHOULD write the issue by describing the problem they face or observe.
* The user SHOULD seek consensus on the accuracy of their observation, and the value of solving the problem.
* Thus, the release history of the project SHALL be a list of meaningful issues logged and solved.
* To work on an issue, a Contributor SHALL fork the project repository and then work on their forked repository.
* To submit a patch, a Contributor SHALL create a Platform pull request back to the project.
* A Contributor SHALL NOT commit changes directly to the project.
* To discuss a patch, people MAY comment on the Platform pull request, on the commit, or elsewhere.
* To accept or reject a patch, a Maintainer SHALL use the Platform interface to merge the patch.
* Maintainers SHOULD NOT merge their own patches except in exceptional cases, such as non-responsiveness from other Maintainers for an extended period (more than 1-2 days).
* Maintainers SHALL NOT make value judgments on correct patches, this is handled by the optional Code Review Process.
* Maintainers SHOULD ask for improvements to incorrect patches and SHOULD reject incorrect patches if the Contributor does not respond constructively.
* Maintainers MAY commit changes to non-source documentation directly to the project.
* The user who created an issue SHOULD close the issue after checking the patch is successful.
* Maintainers SHOULD close user issues that are left open without action for an uncomfortable period of time.

## Code Review Process

* The project MAY use a code review process, particularly if it is a shipping project with non-trivial complexity.
* If code reviews are enabled for the project, Maintainers SHALL NOT merge a patch until a Reviewer has examined and approved the patch.
* If code reviews are not enabled for the project, Maintainers SHALL merge correct patches rapidly.
* Code reviews are not enabled for this project

## Branches and Releases

* The project SHALL have one branch ("master") that always holds the latest in-progress version and SHOULD always build.
* The project SHALL NOT use topic branches for any reason. Personal forks MAY use topic branches.
* To make a stable release someone SHALL fork the repository by copying it and thus become maintainer of this repository.
* Stable releases SHALL always be released from the repository master.
* Forking a project for stabilization MAY be done unilaterally and without agreement of project maintainers.
* Maintainers of the stabilization project SHALL maintain it through pull requests which MAY cherry-pick patches from the forked project.
* A patch to a repository declared "stable" SHALL be accompanied by a reproducible test case.
* A stabilization repository SHOULD progress through these phases: "unstable", "candidate", "stable", and then "legacy". That is, the default behavior of stabilization repositories is to die.

## Evolution of Public Contracts

* All Public Contracts (APIs or protocols) MUST be documented.
* All Public Contracts SHALL use Semantic Versioning [2].
* All Public Contracts SHOULD have space for extensibility and experimentation.
* A patch that modifies a Public Contract SHOULD not break existing applications unless there is prior consensus on the value of doing this.
* A patch that introduces new features SHOULD do so using new names (a new contract).
* New contracts SHOULD be marked as "draft" until they are stable and used by real users.
* Tests for CI/CD automation SHOULD be provided for new contracts to ensure patches are not breaking the contract.
* Old contracts SHOULD be deprecated in a systematic fashion by marking them as "deprecated" and replacing them with new contracts as needed.
* When sufficient time has passed, old deprecated contracts SHOULD be removed.
* Old names SHALL NOT be reused by new contracts.

## Issue Format

* One issue SHOULD address one single identifiable problem or a small set of tightly related problems.
* The issue title SHOULD state the observed problem in minimal fashion. The statement SHOULD start with "Problem:"
* The issue body SHOULD capture all relevant data in a minimal and accurate fashion.
* The issue body MAY propose solutions. The statement SHOULD start with "Solution:"
* Users SHALL NOT log feature requests, ideas, suggestions, or any solutions to problems that are not explicitly documented and provable.

## Task and Role Assignment

* All tasks and roles SHALL be self-assigned, based on individual judgement of the value of taking on a certain task or role.

## Bibliography

1. "Key words for use in RFCs to Indicate Requirement Levels" - [ietf.org](https://tools.ietf.org/html/rfc2119)
2. "Semantic Versioning 2.0.0" - [semver.org](http://semver.org)
