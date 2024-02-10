# Marvin Bot


Marvin is a GitHub Application that can help to automate certain aspects of our work on and beyond GitHub. Currently it offers the following functions:


1. Kata Issue Handling
2. Reminders


These functions are explained below.


## 1. Kata Issue Handling


The bot automatically parses any new issue created for an expected structure. This structure consists of a divider `---` followed by two fields `**due**: YYYY-MM-DD` and `**supervisor**: @supervisor`. The two fields might appear in any order, there might be any number of empty lines in between and additional, unrelated dividers are also accepted. A concise example looks like this:


```
This is a target condition. We want to reach the following state:


- [ ] something is running
- [ ] something else finally broke as expected


---


**due**: YYYY-MM-DD
**supervisor**: @supervisor
```




Once a valid target condition has been detected, the bot will post a timeline-comment. This is usually the first post. It will visualise the timeline of changes. When a due date has expired, the bot will post a friendly reminder asking the author to adjust the due date in the first post. This can be done by editing the first issue and changing the due date. Finally, when the target condition is closed the bot will post a summary.




## 2. Reminders


Sometimes it is useful to get back to issues in after a certain time to re-evaluate. This can be achieved by leveraging marvins command syntax. Each marvin command starts with `/marvin` followed by a specific sub-command, in this case `remind`. When a command has been parsed correctly, marvin will set a "eyes" reaction to indicate that the reminder has been set. On the early morning of the reminder date (UTC), marvin will post a comment and mention the attributed user.


**Examples**


First lets look at some examples, they should be fairly self-explanatory:


```
/marvin remind me in 2 days
/marvin remind me in 3 weeks
/marvin remind me in 4 months
/marvin remind me on 2023-01-18
/marvin remind @plihub in 1d
/marvin remind @plihub in 2w
/marvin remind @plihub in 3m
```


**Syntax**


The more formal syntax is:


```
/marvin remind <attribution> <date>
```


where:


- `attribution` is either "me" or any github user handle starting with an "@"
- `date` is either the word "on" followed by an `<absolute date>` or  the word "in" followed by a `<relative date>`
    - `absolute date` is a date in the form of YYYY-MM-DD
    - `relative date` is a number followed by either a `<day>`, `<week>` or `<month>` identifier
        - `day` is either "day", "days" or "d"
        - `week` is either "week", "weeks" or "w"
        - `month` is either "month", "months" or "m"