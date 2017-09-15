# CMSC389L: Practical Cloud Computing with AWS

![AWS Diagram](media/aws_diagram.png)

## Course Description

This course provides a practical and programming-oriented introduction to cloud computing with [Amazon Web Services](https://aws.amazon.com/about-aws/) (AWS). Students will learn how to build applications using a variety of AWS services, including S3, EC2, Lambda, and Beanstalk. The course will culminate in a final resume-worthy project that will be built, deployed, and demoed.

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
- **Syllabus Last Updated**: September 1, 2017

## Schedule

| Week       | Topic                                    | Codelab    | Project       |
| ---------- | ---------------------------------------- | ---------- | ------------- |
| 9/1/2017   |	Introduction and AWS 101				| Codelab 1  | |
| 9/8/2017   |	Object Storage: S3 						| Codelab 2  | |
| 9/15/2017  |	Content Delivery Networks: CloudFront 	|            |  |
| 9/22/2017  |  Compute 1: EC2							| Codelab 3  | Project 1 Available |
| 9/29/2017  |	Compute 2: EC2							| Codelab 4  | |
| 10/6/2017  | 	Now You're Thinking w/ Queues: SQS		| Codelab 5  |  |
| 10/13/2017 |	Load Balancers: ELB + ALB 				| Codelab 6  | Project 1 Due & Project 2 Available |
| 10/20/2017 |	PaaS: Elastic Beanstalk					| Codelab 7  | |
| 10/27/2017 |	Functions: Lambda	 					| Codelab 8  | |
| 11/3/2017  |	*Midterm*	 							|            | Project 2 Due |
| 11/10/2017 |	APIs: API Gateway	 					| Codelab 9 | Final Project Available |
| 11/17/2017 |	Databases: DynamoDB 					| Codelab 10 | |
| 11/24/2017 |	*Thanksgiving Break (Campus Closed)* 	| 			 | |
| 12/1/2017  |	Containers: ECS					 		| Codelab 11 | |
| 12/8/2017  |  Cloud Security				   			| Codelab 12 | |
| 12/13/2017 |	*No Class*  						    |            | Final Project Due |
| 12/14/2017 |	*No Class*  						    |            | Final Project Video Demos Due |

Learn more about these services in [plain english](https://www.expeditedssl.com/aws-in-plain-english) or from [AWS](https://www.amazonaws.cn/en/products/).

## Projects

- Project 1: TBD (S3, CloudFront, EC2)
- Project 2: TBD (ELB, EC2, SQS)
- Final Project

## Final Project

The final project will be an opportunity to apply all of the knowledge that you have gained into an application that you will build from the ground up. The grading scheme for the final project is TBD, but it will factor in creativity and will require the use of at least three of the major services covered in lecture, including at least one that was not used in a project. Students are welcome to (but not required to) incorporate other AWS services that weren't covered in this course.

Students will be required to record and submit a 2-5 minute video detailing how their project works. More information on the structure of the demo video will be released with the final project's spec. The demo will be due at 11:59:59 PM the day after the final project is due.

## Midterm

There will be one exam in this class, a midterm. It will focus on the concepts taught in class and covered on the in-class worksheets.

## Codelabs

Students will receive a codelab each week at the end of class that will be due at 11:59:59PM the day before class the following week. Codelabs can be submitted on [submit.cs.umd.edu](http://submit.cs.umd.edu).

Codelabs are modeled off of Google's codelabs. They are guided, hands-on coding experiences which will step you through the process of building on top of AWS. They aren't meant to be challenging and are instead meant to help you get your hands dirty with the services we will learn about in class.

## Computing Resources

Students will have access to AWS resources via the [AWS Free Tier](https://aws.amazon.com/s/dm/optimization/server-side-test/free-tier/free_np/), which should be more than enough to cover all of the programming assignments in this course. Students may need to create a new AWS account if they have already used their credit.

Students may also receive access to further resources via [AWS Educate](https://aws.amazon.com/education/awseducate/). More information will be released in the fall.

## Grading

| % Total | Assignment           | Description |
| ------- | -------------------- | ----------- |
| 20%     | Programming Projects | Individual projects that will involve working with AWS services. |
| 20%     | Codelabs             | Graded for completion |
| 10%     | In-class worksheets  | Graded for completion (1 can be dropped) |
| 20%     | Midterm              | The examination will focus on theoretical concepts. |
| 30%     | Final Project + Demo | A free-form final project with a video demo. |

## Administrivia

### Office Hours

| Instructor | Hours               | Location |
| ---------- | ------------------- | -------- |
| Colin King | Tuesdays 4-5PM, Fridays 2-3PM, or [by appt](mailto:colink@umd.edu).   | AVW 4101      | 

### Project Submission

Projects must be submitted electronically following the instructions given in each project assignment. Projects may not be submitted by any other means (e.g., please do not email your projects to us). It is your responsibility to test your program and verify that it works properly before submitting. All projects are due at 11:59:59 PM on the day indicated on the schedule above.

Projects may be submitted up to 24 hours late for a 20% penalty. If you submit both on-time and late, your project will receive the maximum of the penalty-adjusted scores. Only the last on-time and last late projects will be graded.

Unlike lower-level programming classes, we will not provide you with test cases (e.g., public tests) before projects are due. You will be responsible for developing your own tests and for using appropriate testing techniques. Also, we expect your projects to use proper style and documentation.

### Grading Fine Print

Grades will be maintained on the CS department [grades server](https://grades.cs.umd.edu/).

You are responsible for all material discussed in lecture and posted on the class repository, including announcements, deadlines, policies, etc.

Any request for reconsideration of any grading on coursework must be submitted within **one week** of when it is returned. No requests will be considered afterwards.

Up to one in-class worksheet may be dropped, for any reason. If you can document that you were at a hackathon or on-site interview, or had to miss class for any university-approved reason, then notify the course instructor in advance and you will be allowed to turn in the worksheet during the following class.

*Completing the projects is an essential part of the course. Therefore, the course staff reserves the right to fail any student who does not make a good-faith attempt on all course projects.* The requirements for a good-faith attempt will be released with each project.

### Course Staff Communications

Students can interact with the instructors in two ways: in-person during office hours and online via Piazza. Email should only be used for emergencies and not class related questions (e.g., projects).

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
