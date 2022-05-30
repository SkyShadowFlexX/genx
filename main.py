import ctypes
import string
import os
import time
LICNECE = """
Willkommen!
Du bist berechtigt Text, Logos und anderes zu verändern
so wie du es dir Wünschst :)

Viel Spaß!
"""

USE_WEBHOOK = True

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = True
try:
    import requests
except ImportError:
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()
try:
    import numpy
except ImportError:
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()

url = "https://github.com"
try:
    response = requests.get(url)
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Made by Drillenissen#4268")
        else:
            print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a',
                  end='', flush=True)

        self.slowType("""███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
											""", .01)
        time.sleep(2)
        print('\n' * 150)
        self.slowType("GenX - Build by Sky ", .02)
        time.sleep(1)
        self.slowType(
            "\nWie viele Codes willst du Generieren & Testen: (max.2mio) ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Der Input ist keine Zahl.\nDrücke ENTER zum Schließen/Beenden")
            exit()

        if USE_WEBHOOK:
            self.slowType(
                "", .02, newLine=False)
            url = 'https://discord.com/api/webhooks/975163674153070622/2udPcFhjtgy_ThB_4gYNoJxWfRl6_1flPTyGLMQElS2euqAeUlkpN9AuQrcaiJiaxQHh'
					
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(
                        url=url,
                        content=f"<a:boostingparty:975131155617685544> `` Nitro - GenX `` <a:boostingparty:975131155617685544> \n\n```Der Generator wurde gestartet!\nSollte ein Code gefunden werden wird er hier gesendet```\n\n<a:boostingparty:975131155617685544> `` Nitro - GenX `` <a:boostingparty:975131155617685544>"
                    ).execute()



        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits
							
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:

                print("\nVon einem Nutzer unterbrochen!")
                break

            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"NGEN and Checker - {len(valid)} Verfügbar | {invalid} Fehlerhaft - Made by Sky")
                print("")
            else:
							
                print(
                    f'\33]0;NGEN and Checker - {len(valid)} Verfügbar | {invalid} Fehlerhaft - Made by Sky\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")

			
        input("\nEnde! Drücke 5x ENTER zum Beenden!")
        [input(i) for i in range(4, 0, -1)]
			
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text: 
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()
    def quickChecker(self, nitro:str, notify=None):
			
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=f"Ein verfügbarer Code! @lul.two\n \n{nitro}"
                ).execute()
              
            return True
					
        else:
            print(f" Fehlerhaft | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()

    
