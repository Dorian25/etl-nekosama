import pandas as pd
import os


def read_xlsx_file(file_path):
    df_xlsx = pd.read_excel(file_path)

    return df_xlsx, df_xlsx.title.unique().tolist()


def transform(titles_anime, extract_data):
    transform_data = []
    for title in titles_anime:
        anime_data = extract_data.loc[(raw_data['title'] == title), :]

        format_anime = anime_data.format.unique()[0].replace("Format ", "")
        titres_alt = anime_data.titre_alt.unique()[0].split(", ")
        cover_img = anime_data["cover_img-src"].unique()[0]
        synopsis = anime_data.synopsis.unique()[0]
        status = anime_data.status.unique()[0].replace("Status ", "")
        diffusion = anime_data.diffusion.unique()[0].replace("Diffusion ", "").split(" - ")
        diffusion_start = diffusion[0]
        diffusion_end = diffusion[1]

        document = {"Titre": title,
                    "Titres Alternatifs": titres_alt,
                    "Synopsis": synopsis,
                    "Format": format_anime,
                    "Statut": status,
                    "Diffusion": {"début": diffusion_start,
                                  "fin": diffusion_end},
                    "Anime": {"VF": []}}

        for index, episode, link_ep, episode_, link_ep_ in anime_data.loc[:,
                                                           ['num_episode', 'link_wplayer', 'episodes_alt',
                                                            'link_iframe']].itertuples():
            if pd.isna(episode) and pd.isna(link_ep):
                if link_ep_ != "undefined":
                    num_episode = "EPISODE " + episode_.split(" - ")[-1]
                    document['Anime']["VF"].append({num_episode: link_ep_})
            else:
                if link_ep != "undefined":
                    num_episode = episode.replace("Ep.", "EPISODE")
                    document['Anime']["VF"].append({num_episode: link_ep})

        transform_data.append(document)
        print(document)


if __name__ == "__main__":
    files_pages_xlsx = os.listdir("./data")
    anime_titles = []
    raw_data, titles = read_xlsx_file("./data/" + files_pages_xlsx[0])

    transform(titles, raw_data)
    anime_titles += titles
    anime_titles_sorted = sorted(anime_titles)

    """
    for file_page_xlsx in files_pages_xlsx:
        raw_data = read_xlsx_file(file_page_xlsx)
        transform_data = transform(raw_data)
        load_sql_db()
        load_mongo_db()
    """
