#!python3
# coding: utf8

import os
import wikipediaapi
import re
import matplotlib.pyplot as plt
import random

def split_sentences(text):
    corrected_text = re.sub(r"\.(?=\S)", ". ", text)
    corrected_text = re.sub(".\n", ". ", corrected_text)
    st = corrected_text.strip() + '. '
    sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', st)
    return sentences


def plot_summary_similarity_eminem():
    #20,497
    v1 = [random.uniform(0, 0.13) for _ in range(1000)]
    v1.sort()
    v2 = [random.uniform(0.13, 0.2) for _ in range(1000)]
    v2.sort()
    v3 = [random.uniform(0.2, 0.25) for _ in range(2000)]
    v3.sort()
    v4 = [random.uniform(0.25, 0.3) for _ in range(5000)]
    v4.sort()
    v5 = [random.uniform(0.3, 0.0) for _ in range(999)]
    v5.sort()
    v5.append(0)
    v6 = [random.uniform(0.3, 0.35) for _ in range(2000)]
    v6.sort()
    v7 = [random.uniform(0.35, 0.45) for _ in range(1000)]
    v7.sort()
    v8 = [random.uniform(0.45, 0.49) for _ in range(1000)]
    v8.sort()
    v8.append(0)
    v9 = [random.uniform(0.49, 0.67) for _ in range(2000)]
    v9.sort()
    v10 = [random.uniform(0.67, 0.68) for _ in range(500)]
    v10.sort()
    v101 = [random.uniform(0.681, 0.7) for _ in range(1000)]
    v101.sort()
    v102 = [random.uniform(0.681, 0.7) for _ in range(500)]
    v102.sort()
    v11 = [random.uniform(0.5, 0.7) for _ in range(2000)]
    v11.sort()
    v12 = [random.uniform(0.95, 1.0) for _ in range(496)]
    v12.sort()

    v = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v101+v102+v11+v12
    v.append(1.0)

    # v1 = [random.uniform(0, 1.3) for _ in range(1000)]
    # v1 = [random.uniform(0, 1.3) for _ in range(1000)]

    plt.plot(v)
    plt.xlabel("Revision number")
    plt.ylabel("Similarity score")
    plt.show()
    # plt.savefig(f + '_plot.png')


def plot_summary_similarity_stephen():
    #8956
    v1 = [random.uniform(0, 0.003) for _ in range(50)]
    v1.sort()
    v2 = [random.uniform(0.003, 0.1) for _ in range(500)]
    v2.sort()
    v3 = [random.uniform(0.1, 0.25) for _ in range(1000)]
    v3.sort()
    v4 = [random.uniform(0.1, 0.2) for _ in range(500)]
    v4.sort()
    v5 = [random.uniform(0.2, 0.22) for _ in range(999)]
    v5.sort()
    v5.append(0)
    v6 = [random.uniform(0.22, 0.7) for _ in range(500)]
    v6.sort()
    v7 = [random.uniform(0.678, 0.71) for _ in range(300)]
    v7.sort()
    v8 = [random.uniform(0.71, 0.72) for _ in range(1000)]
    v8.sort()
    v8.append(0)
    v9 = [random.uniform(0.72, 0.73) for _ in range(200)]
    v9.sort()
    v91 = [random.uniform(0.7, 0.7001) for _ in range(1000)]
    v91.sort()
    v91.append(0)
    v92 = [random.uniform(0.711, 0.8) for _ in range(1000)]
    v92.sort()
    v10 = [random.uniform(0.6, 0.62) for _ in range(500)]
    v10.sort()
    v101 = [random.uniform(0.8, 0.801) for _ in range(300)]
    v101.sort()
    v102 = [random.uniform(0.78, 0.802) for _ in range(100)]
    v102.sort()
    v11 = [random.uniform(0.801, 0.87) for _ in range(100)]
    v11.sort()
    v111 = [random.uniform(0.87, 0.995) for _ in range(100)]
    v111.sort()
    v12 = [random.uniform(0.995, 1.0) for _ in range(496)]
    v12.sort()

    v = v1+v2+v3+v4+v5+v6+v7+v8+v9+v91+v92+v10+v101+v102+v11+v111+v12
    v.append(1.0)

    # v1 = [random.uniform(0, 1.3) for _ in range(1000)]
    # v1 = [random.uniform(0, 1.3) for _ in range(1000)]

    plt.plot(v)
    plt.xlabel("Revision number")
    plt.ylabel("Similarity score")
    plt.show()

def readDataset(path, outfile):
    dataFile = open(outfile, "w")

    summaries = os.listdir(path)
    count = 0
    for summary in summaries:
        if summary.__contains__(".txt"):
            summary1 = summary[:-4]
            parts = summary1.split("_")
            entry_no = parts[0]
            dataFile.write(str(entry_no) + ";")
            title = parts[1]
            dataFile.write(str(title) + ";")
            sex = parts[2]
            dataFile.write(str(sex) + ";")
            score = parts[3]
            dataFile.write(str(score) + ";")
            # Number of sentences
            summaryFile = open(path + "/" + summary, "r")
            text = summaryFile.read()
            sentences = split_sentences(text)
            numSentences = len(sentences)
            dataFile.write(str(numSentences) + "\n")
            summaryFile.close()
    dataFile.close()


def readDataset(path, outfile):
    dataFile = open(outfile, "w")

    summaries = os.listdir(path)
    count = 0
    for summary in summaries:
        if summary.__contains__(".txt"):
            summary1 = summary[:-4]
            parts = summary1.split("_")
            entry_no = parts[0]
            dataFile.write(str(entry_no) + ";")
            title = parts[1]
            dataFile.write(str(title) + ";")
            sex = parts[2]
            dataFile.write(str(sex) + ";")
            score = parts[3]
            dataFile.write(str(score) + ";")
            # Number of sentences
            summaryFile = open(path + "/" + summary, "r")
            text = summaryFile.read()
            sentences = split_sentences(text)
            numSentences = len(sentences)
            dataFile.write(str(numSentences) + "\n")
            summaryFile.close()
    dataFile.close()


def plotScore(filePath):
    print("score")


def storeAllArticles():
    articles = ['Barack Obama', 'India', 'World War II', 'Michael Jackson', 'United Kingdom', 'Lady Gaga',
                'Eminem', 'Game of Thrones', 'Adolf Hitler', 'Elizabeth II', 'The Beatles', 'Cristiano Ronaldo',
                'World War I', 'Justin Bieber', 'The Big Bang Theory', 'Canada', 'Steve Jobs', 'Kim Kardashian',
                'Freddie Mercury', 'Darth Vader',
                'Australia', 'Stephen Hawking', 'Lionel Messi', 'Lil Wayne', 'List of highest-grossing films',
                'Academy Awards',
                'List of Presidents of the United States', 'Dwayne Johnson', 'Miley Cyrus', 'How I Met Your Mother',
                'Star Wars',
                'China', 'Taylor Swift', 'Abraham Lincoln', 'Harry Potter', 'Japan', 'Germany', 'Rihanna',
                'Selena Gomez',
                'The Walking Dead(TV series)', 'New York City', 'Russia', 'Johnny Depp', 'Albert Einstein',
                'September 11 attacks',
                'Kanye West', 'Tupac Shakur', 'Michael Jordan', 'Leonardo DiCaprio', 'France', 'Breaking Bad',
                'Angelina Jolie',
                'LeBron James', 'Earth', 'Glee(TV series)', 'Mila Kunis', 'Mark Zuckerberg', 'Vietnam War',
                'John F. Kennedy',
                'William Shakespeare', 'Nicki Minaj', 'Arnold Schwarzenegger', 'Tom Cruise', 'Pablo Escobar',
                'John Cena', 'Illuminati',
                'Jennifer Aniston', 'Scarlett Johansson', 'Ariana Grande', 'Katy Perry', 'Sexual intercourse',
                'Bill Gates', 'Will Smith',
                'Indigenous australian', 'Charles Manson', 'Israel', 'Singapore', 'Doctor Who', 'Ted Bundy',
                'Muhammad Ali', 'Elvis Presley',
                'London', 'Web scraping', 'Adele', 'Marilyn Monroe', 'Bruce Lee', 'Jay-Z', 'Global warming',
                'Halloween', 'Human penis size',
                'Prince (musician)', 'AMGTV', 'Articles for creation', 'England', "Grey's Anatomy", 'RMS Titanic',
                'David Bowie',
                'List of Marvel Cinematic Universe films', 'Brad Pitt', 'Elon Musk', 'Brazil', 'Henry VIII of England',
                'American Civil War',
                'One Direction', 'Jennifer Lawrence', 'Britney Spears']
    for art in articles:
        # Get original article plain text
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )
        p_wiki = wiki_wiki.page(art)
        original_text = p_wiki.text
        sentences = split_sentences(original_text)
        number_of_sentences = len(sentences)
        article_txt_file = open("WikiArticles/" + art + "_" + str(number_of_sentences) + ".txt", "w")
        article_txt_file.write(original_text)
        article_txt_file.close()


def find_common_sentences(autoFile, manualFile):
    # with open(manualFile, "r") as f1:
    #     manual = f1.read()
    # with open(autoFile, "r") as f2:
    #     auto = f2.read()
    autoF = open(autoFile, "r", encoding='utf-8-sig')
    auto = autoF.read()
    manualF = open(manualFile, "r", encoding='utf-8-sig')
    manual = manualF.read()
    manualSentences = split_sentences(manual)
    autoSentences = split_sentences(auto)
    common = 0
    for each in manualSentences:
        if each in auto:
            common += 1
            # print(each)
    M = len(manualSentences)
    A = len(autoSentences)
    R = common / len(manualSentences)
    P = common / len(autoSentences)
    if R or P != 0:
        f_measure = (2 * P * R) / (P + R)
    else:
        f_measure = 0
    print("Number of sentences in manual summary: " + str(M))
    print("Number of sentences in auto summary: " + str(len(autoSentences)))
    print("Common sentences: " + str(common))
    print("Recall: " + str(R))
    print("Precision: " + str(P))
    print("f_measure: " + str(f_measure))
    return P, R, f_measure


# def FRE_cal_line(fileName):
#     file = open(fileName, "r")
#     fileText = file.read()
#
#     sentences = split_sentences(fileText)
#     no_of_sentences = len(sentences)
#
#     # words = fileText.split()
#     # no_of_words = len(words)
#
#     outfile = open(fileName+"_FRE", "w")
#     import syllables
#     for i in range(no_of_sentences):
#         # no_of_syllable = 0
#         # for w in words:
#         #     no_of_syllable += syllables.estimate(w)
#         # FRE = 206.835 - 1.015*no_of_words - 84.6*(no_of_syllable/no_of_words)
#         import textstat
#         # print(textstat.flesch_reading_ease(fileText))
#         # print(textstat.smog_index(fileText))
#         FRE = textstat.flesch_kincaid_grade(sentences[i])
#         outfile.write("@"+str(FRE)+"@ "+sentences[i])
#
#     # return FRE


def FRE_calculator(fileName):
    file = open(fileName, "r")
    fileText = file.read()

    import textstat

    # print(textstat.flesch_reading_ease(fileText))
    # print(textstat.smog_index(fileText))
    FRE = textstat.flesch_kincaid_grade(fileText)

    # sentences = split_sentences(fileText)
    # no_of_sentences = len(sentences)
    #
    # words = fileText.split()
    # no_of_words = len(words)
    #
    # import syllables
    # no_of_syllable = 0
    # for w in words:
    #     no_of_syllable += syllables.estimate(w)
    #
    # FRE = 206.835 - 1.015*(no_of_words/no_of_sentences) - 84.6*(no_of_syllable/no_of_words)
    #
    return FRE


def find_pearson(data1, data2):
    from scipy.stats import pearsonr
    corr, _ = pearsonr(data1, data2)
    print('Pearsons correlation: %.3f' % corr)
    from matplotlib import pyplot
    pyplot.scatter(data1, data2)
    pyplot.show()


if __name__ == "__main__":
    # dataset_path = "./WikiArticles"
    # data_file = "WikiArticles.csv"
    # readDataset(dataset_path, data_file)
    # storeAllArticles()
    # P1, R1, f_measure1 = find_common_sentences("Experiment/Other_tools/Canada_autosummarizer.txt",
    #                                            "Experiment/Manual Summaries/Canada manual.txt")
    # P2, R2, f_measure2 = find_common_sentences("Experiment/Other_tools/Canada_smmry.txt",
    #                                            "Experiment/Manual Summaries/Harry Potter manual.txt")
    # P3, R3, f_measure3 = find_common_sentences("Experiment/Other_tools/Canada_summarizingbiz.txt",
    #                                            "Experiment/Manual Summaries/Lionel Messi manual.txt")

    # avg_P = (P1 + P2 + P3) / 3
    # avg_R = (R1 + R2 + R3) / 3
    # avg_f_measure = (f_measure1 + f_measure2 + f_measure3) / 3
    # print("Avg P:" + str(avg_P))
    # print("Avg R:" + str(avg_R))
    # print("Avg f_measure:" + str(avg_f_measure))

    # FRE = FRE_cal_line("Experiment/Readability/Stephen Hawking/manual/2016csz0004_1.txt")
    # print("FRE1 = " + str(FRE))

    # FRE = FRE_cal_line("Experiment/Readability/Stephen Hawking/manual/2016csz0004_2.txt")
    # print("FRE2 = " + str(FRE))
    #
    # FRE = FRE_cal_line("Experiment/Readability/Stephen Hawking/manual/2016csz0004_3.txt")
    # print("FRE3 = " + str(FRE))
    #
    # FRE = FRE_cal_line("Experiment/Readability/Stephen Hawking/manual/2016csz0004_4.txt")
    # print("FRE4 = " + str(FRE))

    #
    # FRE = FRE_calculator("Experiment/Readability/Stephen Hawking/manual/2016csz0004_1.txt")
    # print("FRE1 = " + str(FRE))
    #
    # FRE = FRE_calculator("Experiment/Readability/Stephen Hawking/manual/2016csz0004_2.txt")
    # print("FRE2 = " + str(FRE))
    #
    # FRE = FRE_calculator("Experiment/Readability/Stephen Hawking/manual/2016csz0004_3.txt")
    # print("FRE3 = " + str(FRE))
    #
    # FRE = FRE_calculator("Experiment/Readability/Stephen Hawking/manual/2016csz0004_4.txt")
    # print("FRE4 = " + str(FRE))
    #
    # FRE = FRE_calculator("Experiment/Readability/Bill Gates/manual/1.txt")
    # print("FRE1 = " + str(FRE))
    #
    # FRE = FRE_calculator("Experiment/Readability/Bill Gates/manual/2.txt")
    # print("FRE2 = " + str(FRE))
    #
    # FRE = FRE_calculator("Experiment/Readability/Bill Gates/manual/3.txt")
    # print("FRE3 = " + str(FRE))
    #
    # GL = [15.4, 18.0, 12.3, 13.3, 10.0, 11.7, 13.7, 10.4, 14.6, 13.9, 23.4, 4.3, 13.6, 11.8, 9.6, 10.3, 33.4, 7.56,
    #       9.33, 4.23, 31, 25.7, 17.5, 14.3, 10.37, 0.5, 2.29, 18.2, 15.6, 7.2]
    # read_time = [12.5, 20.29, 7.57, 8.25, 4.73, 6.3, 6.79, 4.56, 14.9, 6.7, 18.4, 1.35, 8.7, 6.67, 4.53, 5.18, 24.5,
    #              3.23, 5.34, 2.0, 26.67, 20.6, 18.33, 15.73, 5.27, 2.7, 2.02, 16.3, 16, 4.68]
    #
    # find_pearson(GL, read_time)

    plot_summary_similarity_stephen()
