module Subject.Subject exposing (..)
import Subject.Model exposing (..)

update : Msg -> SubjectModel -> (SubjectModel, Cmd Msg)
update msg model =
    case msg of 
        _ ->
            ( model, Cmd.none )
