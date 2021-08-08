module Subject.Model exposing (..)
import Utils.Lang exposing (MultiLangText)
import Url.Parser.Query exposing (Parser, int, map)
import Aspect.Model
import Url exposing (Url)


-- MSG

type Msg
    = InitMsg Url
    | Msg1


-- Model


type alias SubjectModel =
    { results : Result String (List Subject)  -- TODO: StringをHttp.Errorに
    , filter : Filter
    }


type alias Subject =
    { title : MultiLangText
    , time : MultiLangText
    , aspect : Aspect.Model.Aspect
    , gakki : MultiLangText
    , teachers : List MultiLangText
    , tanni : Int
    , place : MultiLangText
    , gakubu : MultiLangText
    , description : MultiLangText
    , link : MultiLangText  -- Japanese Link, English Link
    }


type alias Filter =
    { aspectId : Maybe Int
    }




-- FUNC


fakeModel : SubjectModel
fakeModel =
    SubjectModel
        (Ok (List.repeat 10 fakeSubject))
        (Filter <| Just 1)


fakeSubject : Subject
fakeSubject =
    Subject
        (MultiLangText "創造システム理論" "Creative System Theory")
        (MultiLangText "金4・5限" "Fri 4・5")
        (Aspect.Model.Aspect 1  (MultiLangText "自然言語" "Natural Language") [])
        (MultiLangText "2021年度 春学期" "2021 Spring")
        ([MultiLangText "井庭 崇" "Takashi Iba", MultiLangText "若新雄純" "Yujun Wakashin"])
        2
        (MultiLangText "オンライン・SFC" "Online/SFC")
        (MultiLangText "総合・環境" "Policy/Information")
        (MultiLangText (String.repeat 10 "これからの時代は, 様々なほげほげ") (String.repeat 10 "Hogefuga piyopiyo"))
        (MultiLangText "www.google.co.jp" "www.google.co.uk")


clearFilter : Filter
clearFilter =
    Filter
        Nothing


subjectQueryParser : Parser Filter
subjectQueryParser =
    map Filter
        (int "aspect")
