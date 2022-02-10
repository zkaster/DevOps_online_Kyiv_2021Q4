Continuous deployement (непрерывное развёртывание отвечает за то, чтобы весь новый функционал после тестирования сразу же попал в основную программу без ручного вмешательства инженеров DevOps)

1. Install proxmox on local server (hardware) 192.168.18.211:8006
2. Make NAT over core-router Mikrotik 4011  
	chain=dstnat action=dst-nat to-addresses=192.168.18.211 to-ports=8006 protocol=tcp dst-address=195.69.76.131 in-interface=ether1_WAN dst-port=11000 log=no log-prefix=""
3. Download iso(Ubuntu server) from official site by link
4. 
	sudo apt instal docker
	sudo apt instal docker.io
	sudo docker network create jenkins
	//sudo docker image pull docker:dind
	docker image pull jenkins/jenkins:lts
	docker volume create j_volume
	docker container run -d -p 8080:8080 -v j_volume:/var/jenkins_home --name jenkins-local jenkins/jenkins:lts
	sudo docker ps //To check is container running?
5. Have to add rule to NAT (core-router Mikrotik 4011) to see jenkins from Internet
	 ;;; jenkins_conatianer
	 chain=dstnat action=dst-nat to-addresses=192.168.18.35 to-ports=8080 protocol=tcp dst-address=195.69.76.131 in-interface=ether1_WAN dst-port=18080 log=no log-prefix="" 
6. Check Jenkins over Internet (http://195.69.76.131:18080) - <<picture3.png>>
7. To get default admin password
	docker container exec 23096cdb9f46 sh -c "cat /var/jenkins_home/secrets/initialAdminPassword"	
	<<picture 4>>
8. Install suggested plugins and change password (zkaster :: ip)
9. Add pluggin "multijob", "locale" and set up "dot use browser language"
10.  Check if all right with jenkins files, which saved in j_volume and remove ontainer instance
	sudo docker container kill 23096cdb9f46 
	sudo docker container rm 23096cdb9f46
11. Start container with Jenkins 
	sudo docker container run -d -p 8080:8080 -v j_volume:/var/jenkins_home --name jenkins-local jenkins/jenkins:lts
	sudo docker container run -d -p 8080:8080 -v j_volume:/var/jenkins_home --name jenkins-local jenkins/jenkins:lts
	And password didnot save and we have to do all steps again with password and settings
	
12. Add job. Used GitHub+AWS Elastic Beanstalk pluggin
	Job steps listed on picture5_*.png
	Also have to create credentials for access to github (github+ git link over SSH) and credentials for AWS

13. AWS Elastic Beanstalk we use for deployment and for running EC2 instance with PHP 8.0. We use freetier version, but in commercial version we can use a couple instanses and to deploye on them at one time or one after successed previos.
	Configuration of AWS Beanstalk showed on picture6_*.png
14. Results of CD showen in Jenkins console file Jenkins_console.log

Jenkins 
https://rangle.io/blog/running-jenkins-and-persisting-state-locally-using-docker-2/

Docker
https://habr.com/ru/company/flant/blog/336654/
