import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class Llama:

    model_path = r"C:\Users\delan\Model_Binary\nsql-llama-2-7B.sav"
    model_id = "NumbersStation/nsql-llama-2-7B"

    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_path, torch_dtype=torch.bfloat16
        )

    def context() -> str:
        templet = """CREATE TABLE stadium (
                    stadium_id number,
                    location text,
                    name text,
                    capacity number,
                    highest number,
                    lowest number,
                    average number
                )

                CREATE TABLE singer (
                    singer_id number,
                    name text,
                    country text,
                    song_name text,
                    song_release_year text,
                    age number,
                    is_male others
                )

                CREATE TABLE concert (
                    concert_id number,
                    concert_name text,
                    theme text,
                    stadium_id text,
                    year text
                )

                CREATE TABLE singer_in_concert (
                    concert_id number,
                    singer_id text
                )

                -- Using valid SQLite, answer the following questions for the tables provided above.

                -- {} ?

                SELECT"""
        return templet

    def inference(self, question) -> str:
        #  = "What is the maximum, the average, and the minimum capacity of stadiums"

        text = self.context().format(question)
