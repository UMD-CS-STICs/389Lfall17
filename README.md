# CMSC389L: Practical Cloud Computing with AWS

![AWS Diagram](media/aws_diagram.png)

## Course Description

This course provides a practical and programming-oriented introduction to cloud computing with [Amazon Web Services](https://aws.amazon.com/about-aws/) (AWS). Students will learn how to build applications using a variety of AWS services, including S3, EC2, Lambda, and Beanstalk. The course will culminate in a final resume-worthy project that will be built, deployed, and demoed.

[Check out the final projects](/vagrant/final-project/projects.md) that came out of this class!

## Course Goals

There are two primary goals of this class:

- For students to become comfortable using and interconnecting the many AWS primitives.
- For students to build a project from scratch using the knowledge they've gained, which can be demoed to prospective employers.

There is also a secondary goal, though it will not play as big of a role in this version of the class:
- To introduce students to scalable design patterns that can be used to design efficient systems.

By the end of the semester, the above diagram will make sense to you and you will have all of the necessary skills to be able to replicate it.

## Course Details

- **Course**: CMSC389L
- **Links**: [[Testudo](https://ntst.umd.edu/soc/search?courseId=CMSC389L&termId=201708&courseStartCompare=&courseStartMin=&courseStartAM=)] [[GitHub](https://github.com/UMD-CS-STICs/389Lfall17)] [[GitBook](https://umd-cs-stics.gitbooks.io/cmsc389l-fall2017/content/)] [[Piazza](https://piazza.com/class/j6r4ozi6uu75px)]
- **Prerequisites**: C- or better in **CMSC330** and CMSC250
- **Credits**: 1
- **Seats**: 30
- **Lecture Time**: Fridays, 1-1:50PM
- **Location**: CSI 3118
- **Semester**: Fall 2017
- **Textbook**: None
- **Course Facilitator**: [Colin King](https://www.linkedin.com/in/colinking1/)
- **Faculty Advisor**: [Neil Spring](http://www.cs.umd.edu/~nspring/)

## Schedule

| Week       | Topic                                    | Codelab    |
| ---------- | ---------------------------------------- | ---------- |
| 9/1/2017   |	Introduction and AWS 101				| [Codelab 1](lectures/lecture-01/codelab.md)  |
| 9/8/2017   |	Object Storage: S3 						| [Codelab 2](lectures/lecture-02/codelab.md)  |
| 9/15/2017  |	Content Delivery Networks: CloudFront 	|            |
| 9/22/2017  |  Compute 1: EC2							|            |
| 9/29/2017  |	Compute 2: EC2							| [Codelab 3](lectures/lecture-05/codelab/README.md)  |
| 10/6/2017  | 	Now You're Thinking w/ Queues: SQS		| [Codelab 4](vagrant/codelabs/codelab-04/README.md)  |
| 10/13/2017 |	Load Balancers: ALBs 				    | Codelab 5  |
| 10/20/2017 |	(Class Canceled)					    |            |
| 10/27/2017 |	FaaS: Lambda	 					    | Codelab 6  |
| 11/3/2017  |	APIs: API Gateway	 				    | Codelab 7  |
| 11/10/2017 |	Databases: DynamoDB	 					| Codelab 8  |
| 11/17/2017 |	Microservices: ECS 					    | Codelab 9  |
| 11/24/2017 |	*Thanksgiving Break (Campus Closed)* 	| 			 |
| 12/1/2017  |  Search: Elasticsearch Service		    | Codelab 10 |
| 12/8/2017  |  Infrastructure as Code: CloudFormation + Terraform | Codelab 11 | 

Learn more about these services in [plain english](https://www.expeditedssl.com/aws-in-plain-english) or from [AWS](https://www.amazonaws.cn/en/products/).

## Final Project

The final project will be an opportunity to apply all of the knowledge that you have gained into an application that you will build from the ground up. The final project is explained in detail [here](vagrant/final-project/README.md).

Students will be required to record and submit a 2-5 minute video detailing how their project works. More information on the structure of the demo video will be released with the final project's spec. The demo will be due at 11:59:59 PM the day after the final project is due.

## Codelabs

Students will receive a codelab each week at the end of class that will be due at 11:59:59PM the day before class the following week. Codelabs can be submitted on [submit.cs.umd.edu](http://submit.cs.umd.edu).

Codelabs are modeled off of Google's codelabs. They are guided, hands-on coding experiences which will step you through the process of building on top of AWS. They aren't meant to be challenging and are instead meant to help you get your hands dirty with the services we will learn about in class.

## Computing Resources

Students will have access to AWS resources via the [AWS Free Tier](https://aws.amazon.com/s/dm/optimization/server-side-test/free-tier/free_np/), which should be more than enough to cover all of the programming assignments in this course. Students may need to create a new AWS account if they have already used their credit. Students will also have access to AWS Educate.

## Grading

| % Total | Assignment           | Description |
| ------- | -------------------- | ----------- |
| 40%     | Codelabs             | Graded for completion |
| 20%     | In-class worksheets  | Graded for completion (1 can be dropped) |
| 40%     | Final Project + Demo | A free-form final project with a video demo. |

## Administrivia

### Office Hours

| Instructor | Hours               | Location |
| ---------- | ------------------- | -------- |
| Colin King | Tuesdays 4-5PM, Fridays 2-3PM, or [by appt](mailto:colink@umd.edu).   | Tuesdays: Sandbox, Fridays: CMSC 3118      |
| Andrej Rasevic | [By appt](mailto:arasevic@cs.umd.edu).   | N/A      |

### Codelab Submission

Codelabs must be submitted electronically following the instructions given in each codelab assignment. codelabs may not be submitted by any other means (e.g., please do not email your codelabs to us). It is your responsibility to test your program and verify that it works properly before submitting. All codelabs are due at 11:59:59 PM on the day indicated in the assignment.

Codelabs may be submitted up to 24 hours late for a 20% penalty. If you submit both on-time and late, your codelab will receive the maximum of the penalty-adjusted scores. Only the last on-time and last late codelabs will be graded.

Unlike lower-level programming classes, we will not always provide you with test cases (e.g., public tests) before codelabs are due. You will be responsible for developing your own tests and for using appropriate testing techniques. Also, we expect your codelabs to use proper style and documentation.

### Grading Fine Print

Grades will be maintained on the CS department [grades server](https://grades.cs.umd.edu/).

You are responsible for all material discussed in lecture and posted on the class repository, including announcements, deadlines, policies, etc.

Any request for reconsideration of any grading on coursework must be submitted within **one week** of when it is returned. No requests will be considered afterwards.

Up to one in-class worksheet may be dropped, for any reason. If you can document that you were at a hackathon or on-site interview, or had to miss class for any university-approved reason, then notify the course instructor in advance and you will be allowed to turn in the worksheet during the following class.

### Course Staff Communications

Students can interact with the instructors in two ways: in-person during office hours and online via Piazza. Email should only be used for emergencies and not class related questions (e.g., codelabs).

### Excused Absence and Academic Accommodations
See the section titled "Attendance, Absences, or Missed Assignments" available at [Course Related Policies](http://www.ugst.umd.edu/courserelatedpolicies.html).

### Disability Support Accommodations

See the section titled "Accessibility" available at [Course Related Policies](http://www.ugst.umd.edu/courserelatedpolicies.html).

### Academic Integrity

Note that academic dishonesty includes not only cheating, fabrication, and plagiarism, but also includes helping other students commit acts of academic dishonesty by allowing them to obtain copies of your work. In short, all submitted work must be your own. Cases of academic dishonesty will be pursued to the fullest extent possible as stipulated by the [Office of Student Conduct](http://osc.umd.edu/OSC/Default.aspx).

It is very important for you to be aware of the consequences of cheating, fabrication, facilitation, and plagiarism. For more information on the Code of Academic Integrity or the Student Honor Council, please visit: [http://www.shc.umd.edu](http://www.shc.umd.edu).

### Course Evaluations

If you have a suggestion for improving this class, don't hesitate to tell the course staff during the semester in-person, over email/Piazza, or through the weekly feedback surveys. At the end of the semester, please don't forget to provide your feedback using the campus-wide CourseEvalUM system. Your comments will help make this class better.

###### Inspired by the [CMSC389K syllabus](https://github.com/CMSC389K/spring17).
