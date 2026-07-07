def find_paper(papers , name):
    index = 0
    for paper in papers:
        if paper == name:
            return index
        else:
            index += 1

paper_name = ["ali","bilai","fazal","hayyan", "hamza","iqbal","musa"]
name = "iqbal"
paper_index = find_paper(paper_name , name)
print(f"{name}'s paper is at {paper_index + 1}th place")