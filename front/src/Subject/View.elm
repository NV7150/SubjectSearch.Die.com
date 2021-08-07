module Subject.View exposing (..)
import Subject.Model exposing (..)
import Model exposing (RootModel)

import Html exposing (..)
import Html.Attributes exposing (..)



view : RootModel -> Html Msg
view model =
    div [ class "subjects-page" ]
        [ text "ueeei"
        ]
