import os
import sys
import subprocess
from subprocess import PIPE, Popen
from docker import *
import docker
from docker.api import container


client = docker.DockerClient.from_env()


def existing_containers():
    docker_ps = "docker ps -a"
    print("\nHere is the containers on your machine\n")
    res = os.system(docker_ps)

    select_container = input("What container do you want to interact with?[Container ID]: ")
    select_container_2 = select_container[:-2]

    select_container_3 = "<Container: {}>".format(select_container_2)
    #print(select_container_2)
    #print(select_container_3)
    #print(client.containers.get(container_id="{}".format(select_container_2) + "23"))
    get_container = client.containers.get(container_id="{}".format(select_container_2))
    #print(str(get_container) == str(select_container_3))

    if str(select_container_3) == str(get_container):
        start_container = input("Start Container?[y/n]: ")
        if start_container == str.casefold("y"):
            print("Starting container")
            container_cmd = str("docker start {}".format(select_container))
            os.system(container_cmd)
            container_att = str("docker attach {}".format(select_container))
            os.system(container_att)
            first_question_fun()

        elif select_container == str.casefold('n'):
            print("")

        else:
            first_question_fun()

    else:
        first_question_fun()
    '''
    con_name = input("What is the name of the container?: ")
    print(client.containers.list(all=True, sparse=True))
    print(client.containers.get(container_id="{}".format(con_name)))
    client.containers.get(container_id="{}".format(select_container))
    '''


def docker_basic():
    def images_fun():
        images_fun_ans = input("\nWhat image would you like to pull?: ")
            
        images = client.images.pull('{}'.format(images_fun_ans))



    while True:
        global image_ans
        image_ans = input("\nWould you like to pull an image?[y/n]: ")
        if image_ans == str.casefold("y"):
            images_fun()
            return image_ans
        elif image_ans == str.casefold("n"):
            ##create docker container##
            first_question_fun()
        else:
            print("**Please enter either y or n**")

def first_question_fun():
    print("1.) Create new container")
    print("2.) Interact with existing one")
    try:
        first_question = int(input("\nDo you want to create new container or interact with an existing one?: "))
        if first_question == 1:
            docker_basic()
        elif first_question == 2:
            existing_containers()
        else:
            print("**Please enter either 1 or 2**")
    except ValueError:
        first_question_fun()
first_question_fun()



