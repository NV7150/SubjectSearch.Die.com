module Model exposing (..)

import Url
import Browser
import Browser.Navigation as Nav
import Url.Parser exposing (Parser, oneOf, s, map, top, (</>), (<?>))
import Utils.Lang exposing (Language)
import Utils.Lang exposing (Language(..))
import Aspect.Model
import Subject.Model
import Subject.Model exposing (Filter)
import Subject.Model exposing (subjectQueryParser)

-- MSG

type Msg
    = UrlRequested Browser.UrlRequest
    | UrlChanged Url.Url
    | AspectMsg Aspect.Model.Msg
    | SubjectMsg Subject.Model.Msg


-- Model

type alias RootModel =
    { key : Nav.Key
    , url : Url.Url
    , lang: Language
    , aspectPage: Aspect.Model.AspectModel
    , subjectPage: Subject.Model.SubjectModel
    }


type Route
    = Home Language
    | AspectIndex Language
    | SubjectPage Language Filter

routeParser : Parser (Route -> a) a
routeParser =
    oneOf
        [ map (Home JA_JP) top
        , map (Home EN_US) (s "en")
        , map (AspectIndex JA_JP) (s "aspect")
        , map (AspectIndex EN_US) (s "en" </> (s "aspect") )
        , map (SubjectPage JA_JP) (s "subjects"  <?> subjectQueryParser)
        , map (SubjectPage EN_US) (s "en" </> (s "subjects" <?> subjectQueryParser))
        ]
