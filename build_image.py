"""Draw the 25 November 2026 news image: a text-first newspaper page.

Layout: a masthead with the date, one lead story, then seven more
stories in two columns. PIL + DejaVu fonts, 1024x1024, no network.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (250, 248, 242)
INK = (20, 20, 20)
RED = (178, 34, 34)
GREY = (90, 90, 90)
RULE = (200, 195, 185)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


STORIES = [
    ("UKRAINE CONFIRMS SHIP STRIKE",
     "Zelenskiy says Ukraine hit a Russian cargo ship in the Gulf of "
     "Finland; ally Norway urges caution over such operations."),
    ("HOUTHI DRONE HITS RIYADH TOWER",
     "A Houthi drone strike on Riyadh's tallest tower wounds 11 people, "
     "Saudi civil defence says, as Yemen's war spills over."),
    ("IRAQ MOVES ON KURDISH OILFIELDS",
     "Iraq's premier orders federal forces to seize oilfields and "
     "crossings in Kurdish-run regions, raising tensions."),
    ("CIA AND ODNI HIT BY CYBER BREACH",
     "US intelligence agencies suffer a cybersecurity breach involving "
     "some unclassified information, a source says."),
    ("TRUMP HONOURS GIULIANI",
     "Donald Trump awards former New York mayor Rudy Giuliani the "
     "Presidential Medal of Freedom at the White House."),
    ("SARKOZY ORDERED TO TRIAL",
     "French officials order ex-president Nicolas Sarkozy and his wife "
     "Carla Bruni to trial in the Libya corruption case."),
    ("REAL MADRID THRASH PSV 5-1",
     "Mbappe scores twice and Bellingham nets a stunner as Real Madrid "
     "overturn a deficit in the Champions League."),
    ("SENEGAL GET AFCON TITLE BACK",
     "Senegal regain their 2025 Africa Cup of Nations title after a "
     "Court of Arbitration for Sport ruling."),
]


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Masthead
    d.text((32, 26), "THE WORLD IN ONE PAGE", font=font(SERIF_B, 44), fill=INK)
    d.text((32, 82), "WEDNESDAY 25 NOVEMBER 2026", font=font(SANS_B, 30), fill=RED)
    d.line([(32, 128), (992, 128)], fill=RULE, width=3)
    d.text((32, 140), "Eight stories from around the world, reported today.",
           font=font(SANS, 22), fill=GREY)
    d.line([(32, 176), (992, 176)], fill=RULE, width=2)

    # Lead story, full width
    y = 196
    title, body = STORIES[0]
    d.text((32, y), title, font=font(SERIF_B, 34), fill=INK)
    y += 48
    for line in wrap(d, body, font(SANS, 26), 960):
        d.text((32, y), line, font=font(SANS, 26), fill=INK)
        y += 34
    y += 14
    d.line([(32, y), (992, y)], fill=RULE, width=2)
    y += 18

    # Seven more stories, two columns
    col_w, gap = 460, 40
    xs = [32, 32 + col_w + gap]
    ys = [y, y]
    for i, (title, body) in enumerate(STORIES[1:]):
        col = i % 2
        x, yy = xs[col], ys[col]
        d.text((x, yy), title, font=font(SERIF_B, 22), fill=INK)
        yy += 32
        for line in wrap(d, body, font(SANS, 20), col_w):
            d.text((x, yy), line, font=font(SANS, 20), fill=INK)
            yy += 27
        ys[col] = yy + 22

    # Footer
    fy = max(ys) + 6
    d.line([(32, fy), (992, fy)], fill=RULE, width=2)
    d.text((32, fy + 12), "Sources: Reuters, Al Jazeera, BBC and others, 25 November 2026.",
           font=font(SANS, 20), fill=GREY)
    img.save("entry.png", "PNG")
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
