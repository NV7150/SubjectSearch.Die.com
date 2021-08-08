module Subject.Subject exposing (..)
import Subject.Model exposing (..)
import Url exposing (Url)
import Url.Parser
import Model



update : Msg -> SubjectModel -> (SubjectModel, Cmd Msg)
update msg model =
    case msg of 
        InitMsg url ->
            -- Update Filter
            case Url.Parser.parse Model.routeParser url of
                Just (Model.SubjectPage _ filter) ->
                    ( { model | filter = filter }
                    , Cmd.none
                    )
                _ ->
                    ( { model | filter = clearFilter }
                    , Cmd.none
                    )
        _ ->
            (model, Cmd.none)
