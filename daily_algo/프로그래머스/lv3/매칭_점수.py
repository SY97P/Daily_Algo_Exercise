import re


class PageInfo:
    def __init__(self, idx, basic_score, links, link_score, match_score):
        self.idx = idx
        self.basic_score = basic_score  # 웹 페이지 텍스트 중 검색어 등장 횟수(대소문자 무시)
        self.links = links
        self.link_score = link_score  # 외부 링크 페이지들의 (basic_score / link_cnt) 합
        self.match_score = match_score  # basic_score + link_score

    def __str__(self):
        return ("idx: {}\nbasic_score: {}\nlinks: {}\nlink_score: {}\nmatch_score: {}"
                .format(self.idx, self.basic_score, self.links, self.link_score, self.match_score))


def solution(word, pages):
    word = word.lower()

    page_dict = {}

    url_regexp = re.compile(r'<meta property=.+content="(https://\S*)"/>')
    token_regexp = re.compile('[a-z]+')
    link_regexp = re.compile(r'<a href="(https://\S*)">')

    for idx, page in enumerate(pages):
        page = page.lower()

        url = url_regexp.search(page).group(1)
        basic_cnt = token_regexp.findall(page).count(word)
        links = link_regexp.findall(page)

        page_dict[url] = PageInfo(idx, basic_cnt, links, 0, basic_cnt)

    for k, v in page_dict.items():
        link_score = v.basic_score / len(v.links) if v.links else 0
        for link in v.links:
            if link not in page_dict:
                continue
            page_dict[link].link_score += link_score
            page_dict[link].match_score += link_score

    return \
    sorted([(pageinfo.match_score, pageinfo.idx) for pageinfo in page_dict.values()], key=lambda x: (-x[0], x[1]))[0][1]


def main():
    answer = solution("blind", [
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
        "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])
    print(answer)


if __name__ == '__main__':
    main()
