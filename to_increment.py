import time




def main():

    n = RequestNum()


    for i in range(n):

        i = i + 1

        time.sleep(1)

        print(i)




def RequestNum():

    r = input("Please input number.: ")


    try:

        r = int(r)

    except ValueError:

        print("Please type using half-width characters and enter an integer.")

        r = RequestNum()

    finally:

        return r




if __name__ == "__main__":

    main()

