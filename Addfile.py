import os, shutil, argparse, csv

cwd=os.getcwd()
os.chdir("C:\\Users\\utente\\")
print(os.getcwd())

working_path=os.path.join(cwd+"\\FileOrganizer\\FileOrganizer\\files\\") #mi sposto nella directory desiderata
os.chdir(working_path)
print(os.listdir())

#definisco le cartelle di destinazione:
audio= os.path.join(working_path + "audio")
docs= os.path.join(working_path + "docs")
images= os.path.join(working_path + "images")

# creo l'eseguibile
parser = argparse.ArgumentParser(description="Puoi usare questo programma per spostare i files da una cartella alla sottocartella di appartenenza, differenziandoli in base al tipo di file")
parser.add_argument("target_file", type=str, help="digitare il nome del file completo di estensione")
args = parser.parse_args()


def move_file(target_file):
    '''with open("recap.csv", "a", newline="") as recap:
        colonne = ["name", "type", "size(B)"]
        reader = csv.reader(recap, delimiter=",")
        writer = csv.writer(recap)
        if os.path.getsize("recap.csv") == 0:
            writer.writerows([colonne])'''
    if os.path.isfile(target_file) and target_file in os.listdir(working_path):
        with open("recap.csv", "a", newline="") as recap:
            colonne = ["name", "type", "size(B)"]
            reader = csv.reader(recap, delimiter=",")
            writer = csv.writer(recap)
            if os.path.getsize("recap.csv") == 0:
                writer.writerows([colonne])
            if target_file.endswith(".mp3"):
                writer.writerow([os.path.splitext(target_file)[-2], os.path.splitext(target_file)[-1], os.path.getsize(target_file)])
                print ("Il file è stato spostato con successo e il recap aggiornato correttamente.")
                return shutil.move(target_file, f"{audio}\\{target_file}")
            if target_file.endswith(".txt") or target_file.endswith(".odt"):
                writer.writerow([os.path.splitext(target_file)[-2], os.path.splitext(target_file)[-1], os.path.getsize(target_file)])
                print ("Il file è stato spostato con successo e il recap aggiornato correttamente.")
                return shutil.move(target_file, f"{docs}\\{target_file}")
            if target_file.endswith(".jpeg") or target_file.endswith(".png") or target_file.endswith("jpg"):
                writer.writerow([os.path.splitext(target_file)[-2], os.path.splitext(target_file)[-1], os.path.getsize(target_file)])
                print ("Il file è stato spostato con successo e il recap aggiornato correttamente.")
                return shutil.move(target_file, f"{images}\\{target_file}")
    else:
        print ("Ops! Pare che il file non esista o non sia stato indicato correttamente.")


move_file(args.target_file)
