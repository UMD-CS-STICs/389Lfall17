# CMSC389_: Practical Cloud Computing

![AWS Diagram](http://community.mis.temple.edu/mis4595sec002fall2015/files/2015/10/AWS.png)

## Course Description

This course provides a practical and project-oriented introduction to cloud computing with [Amazon Web Services](https://aws.amazon.com/about-aws/) (AWS). Students will learn how to build applications using a variety of AWS services, including S3, EC2, Lambda, and Beanstalk. The course will culminate in a final resume-worthy project that will be built, deployed, and demoed to the class.

By the end of the semester, the above diagram will make sense to you and you will have all of the necessary skills to be able to replicate it.

## Course Details

- **Course**: CMSC389_
- **Prerequisites**: C- or better in **CMSC330** and CMSC250
- **Credits**: 1
- **Seats**: TBD
- **Lecture Time**: Fridays, 1-1:50PM
- **Location**: TBD
- **Semester**: Fall 2017
- **Textbook**: None
- **Course Facilitator**: [Colin King](https://www.linkedin.com/in/colinking1/)
- **Faculty Advisor**: [Neil Spring](http://www.cs.umd.edu/~nspring/)
- **Syllabus Last Updated**: May 9, 2017

## Topic List

The following are the proposed topics to be covered. This list will be updated over the summer as the lecture content is developed.

- Introduction to AWS
	- What is/Why Cloud Computing?
	- Overview of AWS Service Categories
	- Usage-based Pricing
	- Regions/Availability Zones/Edge Locations
	- AWS vs. Heroku
- Python Crash Course
- Simple Storage Service (S3)
	- Buckets and Objects
	- Caching w/ CloudFront
	- Cheaper Storage Options (S3-IA, Glacier)
- Elastic Compute Cloud (EC2)
	- Instance Types and Virtualization
	- EBS Volumes
	- Programmatic EC2 Manipulation
- Simple Queue Service (SQS)
- Load Balancers (ELB, ALB)
- Platform as a Service (Elastic Beanstalk)
- Serverless Computing (Lambda)
- API Gateway
- Databases (SimpleDB)
- Containers (EC2 Container Service)
	- Docker
- Cloud Security
	- Identity and Access Management (IAM)
	- Firewalls

Learn more about these services in [plain english](https://www.expeditedssl.com/aws-in-plain-english) or from [AWS](https://www.amazonaws.cn/en/products/).

## Computing Resources

Students will have access to AWS resources via the [AWS Free Tier](https://aws.amazon.com/s/dm/optimization/server-side-test/free-tier/free_np/), which should be more than enough to cover all of the programming assignments in this course. Students may need to create a new AWS account if they have already used their credit.

Students may also receive access to further resources via [AWS Educate](https://aws.amazon.com/education/awseducate/). More information will be released in the fall.

## Schedule

| Week | Topic | Assignment |
| ---- | ----- | ---------- |
| 9/1/2017 |	Introduction and Python 101 | |
| 9/8/2017 |	Object Storage: S3	 | Project 0 |
| 9/15/2017 |	Content Delivery Networks: CloudFront | |
| 9/22/2017 | Compute: EC2	| |
| 9/29/2017 |	 Compute: EC2	 | Project 1 |
| 10/6/2017 | 	Now You're Thinking w/ Queues: SQS | |
| 10/13/2017 |	Load Balancers: ELB + ALB | |
| 10/20/2017 |	PaaS: Elastic Beanstalk | Project 2 |
| 10/27/2017 |	Functions: Lambda	 | |
| 11/3/2017 |	 *Midterm*	 | |
| 11/10/2017 |	APIs: API Gateway	 | |
| 11/17/2017 |	Databases: SimpleDB |	Project 3 |
| 11/24/2017 |	*Thanksgiving Break (Campus Closed)* | |
| 12/1/2017 |	 Containers: EC2 Container Service | |
| 12/8/2017 | 	Cloud Security	| |
| TBD |	Final Exam Period	| Final Project Demos



## Projects

- Project 0: Python Introduction
- Project 1: Dropbox Clone (S3, CloudFront)
- Project 2: TBD (EC2, SQS)
- Project 3: TBD (Lambda, API Gateway)
- Final Project: See Below

## Final Project

The final project will be an opportunity to apply all of the knowledge that you have gained into an application that you will build from the ground up. The grading scheme for the final project is TBD, but it will factor in creativity and will require the use of at least three of the major services covered in lecture. Students are welcome to (but not required to) incorporate other AWS services that weren't covered in this course.

## Grading

| % Total | Assignment           | Description |
| ------- | -------------------- | ----------- |
| 50%     | Programming Projects | Individual projects that will involve working with AWS services. |
| 5%     | In-class exercises | Graded for completion |
| 20%     | Midterm              | The examination will focus on theoretical concepts. |
| 25%     | Final Project + Demo | A free-form final project that will be demoed to the class. |

## Administrivia

### Office Hours

| TA         | Hours |
| ---------- | ----- |
| Colin King | TBD   |

### Project Submission

Projects must be submitted electronically following the instructions given in each project assignment. Projects may not be submitted by any other means (e.g., please do not email your projects to us). It is your responsibility to test your program and verify that it works properly before submitting. All projects are due at 11:59 PM on the day indicated on the schedule above.

Projects may be submitted up to 24 hours late for a 10% penalty. If you submit both on-time and late, your project will receive the maximum of the penalty-adjusted scores. You may submit multiple times.

Unlike lower-level programming classes, we will not provide you with test cases (e.g., public tests) before projects are due. You will be responsible for developing your own tests and for using appropriate testing techniques. Also, we expect your projects to use proper style and documentation.

### Grading Fine Print

Grades will be maintained on the CS department [grades server](https://grades.cs.umd.edu/).

You are responsible for all material discussed in lecture and posted on the class repository, including announcements, deadlines, policies, etc.

Any request for reconsideration of any grading on coursework must be submitted within **one week** of when it is returned. No requests will be considered afterwards.

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

If you have a suggestion for improving this class, don't hesitate to tell the course staff during the semester. At the end of the semester, please don't forget to provide your feedback using the campus-wide CourseEvalUM system. Your comments will help make this class better.

###### Inspired by the [CMSC389K syllabus](https://github.com/CMSC389K/spring17).
