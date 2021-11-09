def start():
        """Teeme valik kellega mängime
        Tagastame m muutuja int formaadis

        :rtype: int
        """
        print("Kivi,Paber,Käärid")
        m=3
        while m not in [1,2]:
            try:
                m=int(input("Kellega mängime?\n1-botid \n2-robotiga"))
            except:
                ValueError
        return m

    def bot_vs_bot(v1:list,v2:list):
        """Robotite mäng
        Tagastame m muutuja int formaadis
        :param list v1: järjend esimese roboti jaoks
        :param list v2: järjend teise roboti jaoks

        """
        while True:
            print("Kas mängime?esc-välja,enter-mängime")
