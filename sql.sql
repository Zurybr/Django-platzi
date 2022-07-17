CREATE TABLE public.skills
(
    skill_id integer NOT NULL,
    skill_name character varying NOT NULL,
    skill_description character varying,
    category_id integer NOT NULL,
    CONSTRAINT skill_id PRIMARY KEY (skill_id),
    CONSTRAINT "categorY_id" FOREIGN KEY (category_id)
        REFERENCES public.categories (category_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE IF EXISTS public.skills
    OWNER to root;